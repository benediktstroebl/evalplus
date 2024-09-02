
def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    
    def diff(a,b):
        if a == b:
            return 0
        return abs(a - b)

    # this works
    # but is soooooooooooooo slow!
    # first idea was to write a function that calculates the difference between two lists
    # e.g. 
    # diff([1,2,3,4,5,1], [1,2,3,4,2,-2])
    # -> [0,0,0,0,3,3]
    # but this works only for a small amount of guesses/scores
    # diff([0,5,0,0,0,4],[4,1,1,0,0,-2])
    # -> [4,4,1,0,0,6]
    #return [diff(g,s) for g,s in zip(guess,game)]
    
    # so instead I am using a list comprehension to first calculate the difference between
    # the scores and the guesses and then return this list
    return [abs(g - s) for g,s in zip(guess,game)]
    
    # this is what I was initially trying to do
    #return [map(lambda x,y: abs(x-y), guess, game)]
