from bpython import importcompletion

import unittest

class TestSimpleComplete(unittest.TestCase):
    def setUp(self):
        self.original_modules = importcompletion.modules
        importcompletion.modules = ['zzabc', 'zzabd', 'zzefg', 'zzabc.e', 'zzabc.f']
    def tearDown(self):
        importcompletion.modules = self.original_modules
    def test_simple_completion(self):
        self.assertEqual(importcompletion.complete(10, 'import zza'), ['zzabc', 'zzabd'])
    def test_package_completion(self):
        self.assertEqual(importcompletion.complete(13, 'import zzabc.'), ['zzabc.e', 'zzabc.f', ])


class TestRealComplete(unittest.TestCase):
    def setUp(self):
        [_ for _ in importcompletion.find_iterator]
        __import__('sys')
        __import__('os')
    def tearDown(self):
        importcompletion.find_iterator = importcompletion.find_all_modules()
        importcompletion.modules = set()
    def test_from_attribute(self):
        self.assertEqual(importcompletion.complete(19, 'from sys import arg'), ['argv'])
    def test_from_attr_module(self):
        self.assertEqual(importcompletion.complete(9, 'from os.p'), ['os.path'])
    def test_from_package(self):
        self.assertEqual(importcompletion.complete(17, 'from xml import d'), ['dom'])


