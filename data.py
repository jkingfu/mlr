import sys
from random import random
n = int(sys.argv[1])
for i in range(n):
    x = 2 * random() - 1.0
    y = 2 * random() - 1.0
    label=1
    if abs(x) + abs(y) < 1.0:
        label = 0
    print str(label) + " x:" + str(x) + " y:" + str(y)

