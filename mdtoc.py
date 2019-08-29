#!/usr/bin/env python
"""
Table of content generator of markdown slides
"""

import re
import sys

__version__ = "0.0.2"


def mdtoc(src):

    hn = [r'name:\s+(\w+)$'] + [r'#'*i + r' (\w+)' for i in range(1, 5)]

    toc = ""
    for line in src:
        name_line = re.match(hn[0], line)
        if name_line:
            slide_name = name_line.group(1)

        # h1 = re.match(r'# (\w+)$', line)
        h1 = re.match(hn[1], line)
        if h1:
            section_name = h1.group(1)
            toc += f"* [{section_name}](#{slide_name})\n"

        h2 = re.match(hn[2], line)
        if h2:
            section_name = h2.group(1)
            toc += f"    + [{section_name}](#{slide_name})\n"

        h3 = re.match(hn[3], line)
        if h3:
            section_name = h3.group(1)
            toc += f"        - [{section_name}](#{slide_name})\n"

        h4 = re.match(hn[4], line)
        if h4:
            section_name = h4.group(1)
            toc += f"            ^ [{section_name}](#{slide_name})\n"

    return toc


def main():
    print(mdtoc(open(sys.argv[1])))


if __name__ == "__main__":
    main()
