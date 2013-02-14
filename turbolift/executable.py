#!/usr/bin/env python

# - title        : Upload for Swift(Rackspace Cloud Files)
# - description  : Want to upload a bunch files to cloud files? This will do it.
# - License      : GPLv3+
# - author       : Kevin Carter
# - date         : 2011-11-09
# - notes        : This is a Swift(Rackspace Cloud Files) Upload Script
# - Python       : >= 2.6

"""
License Information

This software has no warranty, it is provided 'as is'. It is your
responsibility to validate the behavior of the routines and its
accuracy using the code provided. Consult the GNU General Public
license for further details (see GNU General Public License).

http://www.gnu.org/licenses/gpl.html
"""

import sys
import os
import time
import itertools
from multiprocessing import Process, freeze_support, Manager

# Local Files to Import
from turbolift.operations import generators, baseofoperations, novacommands
from turbolift import arguments, info


def run_turbolift():
    """
    This is the run section of the application Turbolift.
    """
    freeze_support()
    tur_arg = arguments.GetArguments().get_values()
    try:
        ops = baseofoperations.BaseCamp(tur_arg)

        if tur_arg['con_per_dir']:
            ops.con_per_dir()

        elif tur_arg['archive']:
            ops.archive()
        
        elif tur_arg['upload'] or tur_arg['tsync']:
            ops.file_upload()

    except KeyboardInterrupt:
        print 'Caught KeyboardInterrupt, I\'M ON FIRE!!!!'

if __name__ == "__main__":
    freeze_support()
    run_turbolift()
