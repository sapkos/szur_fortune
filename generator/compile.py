import random

from assets import korwin_wisdom

def fortune(seed=korwin_wisdom):
    print(' '.join(map(random.choice, seed)))
