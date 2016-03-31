#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from romajitools import *

class RTTestCase(unittest.TestCase):
    def test_lemma_tables(self):
        # sanity test
        self.assertEqual(len(LEMMAS), 243)
    
    def test_hiragana_table(self):
        # check that all Hiragana entries have a lemma, and vis versa
        for lemma in TO_HIRA:
            self.assertIn(lemma, LEMMAS,
                    "Lemma from Hiragana table not in master table: {}".format(lemma))
        for lemma in LEMMAS:
            self.assertIn(lemma, TO_HIRA,
                    "Hiragana table missing a lemma: {}".format(lemma))
        
    def test_convert_from_hira(self):
        # sanity test
        self.assertEqual(to_wapuro("ひらがな"), "hiragana")

if __name__ == '__main__':
    unittest.main()