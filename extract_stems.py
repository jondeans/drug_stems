#!/usr/bin/env python

import argparse

def main(args):
    ixe_list = []
    is_first = 1

    with open(args.FILE, 'r') as f:
        for line in f:
            line = line.rstrip('\r\n')
            parts = line.split('\t')    
            
            if parts[0] != '':
                (ixe, desc, ex) = parts
                is_first = 1

                ixes = ixe.split(', ')
                ixe_list.extend(ixes)
            else:
                (_, ixe, desc, ex) = parts

                if is_first:    
                    is_first = 0
                    # del(ixe_list[-1])

                ixes = ixe.split(', ')
                ixe_list.extend(ixes)
    
    ixe_set = set(ixe_list)
    for s in ixe_set:
        print(s)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract regex patterns for common drug endings (suffix, prefix, infix).")
    parser.add_argument("FILE", help="Filename of drug-endings file constructed from druginfo.nlm.nih.gov")

    args = parser.parse_args()
    main(args)