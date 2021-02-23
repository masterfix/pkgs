#!/usr/bin/env python3

import os
import re

lines = os.popen('git diff HEAD~ --name-only').readlines()
p = re.compile('^recipes/([^/]*)/.*$')

pkgs = set()

for line in lines:
  line = line.strip()
  pkgs.update(p.findall(line))

pkgs = sorted(pkgs)

print('\n'.join(pkgs))
