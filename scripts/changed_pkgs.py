#!/usr/bin/env python3

import os

lines = os.popen('git diff HEAD~ --name-only').readlines()

for line in lines:
  line = line.strip()
  print('line:', line)


