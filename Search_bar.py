#Python search bar using Redis as a datastore server.

import math 
import collections
import os
import re
import redis
import unittest

NON_Word = re.compile("[a-z0-9' ]")