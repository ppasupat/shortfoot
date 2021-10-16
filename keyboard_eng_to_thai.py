#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Converts the text typed using the QWERTY layout to Thai Kedmanee.

This is just a thin wrapper over pythainlp
"""

import sys, os, shutil, re, argparse, json
from collections import defaultdict, Counter

from pythainlp.util import eng_to_thai, thai_to_eng


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-i', '--input-col', type=int, default=-1)
    parser.add_argument('-r', '--reverse', action='store_true')
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()

    for line in args.infile:
        cols = line.rstrip('\n').split('\t')
        src = cols[args.input_col]
        if args.reverse:
            tgt = thai_to_eng(src)
        else:
            tgt = eng_to_thai(src)
        print('\t'.join(cols + [tgt]))

    

if __name__ == '__main__':
    main()

