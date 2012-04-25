#!/usr/bin/env python
# -*- coding: utf8 -*-
#  Copyright (c) 2012 Jesse Griffin
#  http://creativecommons.org/licenses/MIT/
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

import os
import sys
from string import punctuation
from operator import itemgetter
from xml.dom import minidom
from collections import defaultdict
from decimal import *


def transform():
  adict = {}
  dictxml = minidom.parse('HebrewMesh.xml')
  for entryxml in dictxml.getElementsByTagName('entry'):
    # get word
    for x in entryxml.getElementsByTagName('w'):
      if x.hasAttribute('xml:lang'):
        word = x.firstChild.data.encode('utf-8')
        if word not in adict:
          adict[word] = []
          break
    # get definitions
    for x in entryxml.getElementsByTagName('def'):
      try:
        mydef = x.firstChild.data.encode('utf-8')
        if mydef not in adict[word]:
          adict[word].append(mydef)
      except: pass
  return adict


if __name__ == '__main__':
  d = transform()
