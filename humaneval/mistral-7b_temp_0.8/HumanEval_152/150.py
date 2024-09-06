
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
    #check how many matches we have
    length = len(game)
    #make sure our guesses are the same size
    if not len(guess) == length:
        return None
    #make our array with the differences
    output = []
    for x in range(0, length):
        #if our guess is equal to the score we add zero
        if game[x] == guess[x]:
            output.append(0)
        #otherwise we add the absolute value of the difference
        else:
            output.append(abs(game[x] - guess[x]))
    return output


















































































































