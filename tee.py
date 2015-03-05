#!/usr/bin/env python
# quick and dirty tee, (w) <github.com/ivanra>
#

import sys

def print_help():
    print('read stdin and output to stdout and given files.\n')
    print('usage: %s [-a] [file ...]' % sys.argv[0])
    print('options:')
    print('  -a - append to files instead of overwriting them.')
    sys.exit(0)

def main():
    mode = 'wb'
    MAX_BUF = 4096
    file_names = []
    for arg in sys.argv[1:]:
        if arg == '-h' or arg == '--help':
            print_help()
        elif arg == '-a':
            mode = 'ab'
        else:
            file_names.append(arg)
    files = [open(fn, mode) for fn in file_names]
    while True: 
        buf = sys.stdin.read(MAX_BUF)
        if not buf:
            break
        for f in files:
            f.write(buf)
        sys.stdout.write(buf)
    for f in files:
        f.flush()
        f.close()
    sys.stdout.flush()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
