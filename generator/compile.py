import random

from assets import korwin_wisdom

def fortune(seed=korwin_wisdom):
    return ' '.join(map(random.choice, korwin_wisdom))
