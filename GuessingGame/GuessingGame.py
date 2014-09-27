__author__ = 'Derek'

from random import randrange

# used randrange instead of randint as it is an alias for the former
# and the extra call can effect performance (not that I really care
# for this program!)
randomNum = randrange(1, 100)

print randomNum
