# This file is part of GAE Testbed (http://gae-testbed.googlecode.com).
# 
# Copyright (C) 2009 JJ Geewax http://geewax.org/
# All rights reserved.
# 
# This software is licensed as described in the file COPYING.txt,
# which you should have received as part of this distribution.

from unit import UnitTestCase
from web import WebTestCase

__all__ = ['FunctionalTestCase']

class FunctionalTestCase(UnitTestCase, WebTestCase):
    pass
