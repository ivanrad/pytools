#!/usr/bin/env python

import sys

def main():
    num = 0
    for line in sys.stdin:
        num += 1
        sys.stdout.write('%d %s' % (num, line))
    sys.stdout.flush()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
