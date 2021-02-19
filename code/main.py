#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import logging 

# set log level to DEBUG
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', 
        level=logging.DEBUG)


def main():
    """ Main entry point of the app """
    logging.debug("hello world")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()