
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
    # check if the number of elements in the guess and score arrays are the same
    if len(game) != len(guess):
        return [None, None, None, None, None, None]
    
    # check if the guess is the same length as the score array
    if len(guess) != len(game):
        return [None, None, None, None, None, None]
    
    # initialize the result array with None
    result = [None, None, None, None, None, None]
    
    # check the first match
    if game[0] != guess[0]:
        result[0] = 0
    
    # check the second match
    if game[1] != guess[1]:
        result[1] = 0
    
    # check the third match
    if game[2] != guess[2]:
        result[2] = 0
    
    # check the fourth match
    if game[3] != guess[3]:
        result[3] = 0
    
    # check the fifth match
    if game[4] != guess[4]:
        result[4] = 0
    
    # check the sixth match
    if game[5] != guess[5]:
        result[5] = 0
    
    # return the result array
    return result

