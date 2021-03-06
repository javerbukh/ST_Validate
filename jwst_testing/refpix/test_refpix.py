"""
py.test module for unit testing the refpix step.
"""

from . import refpix_utils

import os
import ConfigParser

from astropy.io import fits
import pytest

# Set up the fixtures needed for all of the tests, i.e. open up all of the FITS files

@pytest.fixture(scope="module")
def input_hdul(request, config):
    if  config.has_option("refpix", "input_file"):
        curdir = os.getcwd()
        config_dir = os.path.dirname(request.config.getoption("--config_file"))
        os.chdir(config_dir)
        hdul = fits.open(config.get("refpix", "input_file"))
        os.chdir(curdir)
        return hdul
    else:
        pytest.skip("needs refpix input_file")

@pytest.fixture(scope="module")
def output_hdul(request, config):
    if  config.has_option("refpix", "output_file"):
        curdir = os.getcwd()
        config_dir = os.path.dirname(request.config.getoption("--config_file"))
        os.chdir(config_dir)
        hdul = fits.open(config.get("refpix", "output_file"))
        os.chdir(curdir)
        return hdul
    else:
        pytest.skip("needs refpix output_file")

@pytest.fixture(scope="module")
def reference_hdul(output_hdul, config):
    CRDS = '/grp/crds/cache/references/jwst/'
    ref_file = CRDS+output_hdul[0].header['R_BIAS'][7:]
    return fits.open(ref_file)

# Unit Tests

