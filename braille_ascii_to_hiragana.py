#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Converts Braille ASCII to hiragana based on the Japanese Braille system."""

import sys, os, shutil, re, argparse, json
from collections import defaultdict, Counter


def translate(br, br_map):
    answer = []
    while br:
        if br[0] in br_map:
            answer.append(br_map[br[0]])
            br = br[1:]
        elif br[:2] in br_map:
            answer.append(br_map[br[:2]])
            br = br[2:]
        else:
            return None
    return ''.join(answer)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--map-file', default='tables/braille_ascii_to_hiragana.tsv')
    parser.add_argument('-i', '--input-col', type=int, default=-1)
    parser.add_argument('infile')
    args = parser.parse_args()

    with open(args.map_file) as fin:
        br_map = dict(x.strip().split() for x in fin)
    
    with open(args.infile) as fin:
        for line in fin:
            cols = line.rstrip('\n').split('\t')
            br = cols[args.input_col]
            ja = translate(br, br_map)
            if ja:
                print('\t'.join(cols + [ja]))
    

if __name__ == '__main__':
    main()

