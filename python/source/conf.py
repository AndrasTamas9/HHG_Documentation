# Add paths so autodoc can find your project modules
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'HHG Python Interface'
copyright = '2025, Zsuzsanna Balint, Krisztina Joos, Tamas Andras'
author = 'Zsuzsanna Balint, Krisztina Joos, Tamas Andras'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

autodoc_show_sourcelink = True

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
