#!/usr/local/bin/python

import argparse
import os

def parse_args():
   parser = argparse.ArgumentParser()
   parser.add_argument("module_name", help="print the path for the module")
   return parser.parse_args()

def main():
   args = parse_args()
   mod = __import__(args.module_name) 
   print os.path.dirname(mod.__file__)

if __name__ == '__main__':
    main()
