__author__ = 'Derek'
# the guessing game program. Computer generates a random number and
# the player has to try to guess it in as few guesses as possible

from random import randrange

# used randrange instead of randint as it is an alias for the former
# and the extra call can effect performance (not that I really care
# for this program!)
randomNum = randrange(1, 100)
running = True
count = 0

print "This is the guessing game!"

while running:
    guess = int(raw_input('Enter an integer between 1 and 100: '))

    if guess == randomNum:
        print 'Congratulations, you guessed it.'
        count += 1
        running = False
    elif guess < randomNum:
        print 'Higher!'
        count += 1
    else:
        print 'Lower!'
        count += 1
else:
    print '\nThe game is over. You got the right answer in {} guess(es)\n'.format(count)

print 'Done'