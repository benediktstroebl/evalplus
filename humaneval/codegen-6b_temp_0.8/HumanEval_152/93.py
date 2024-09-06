
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
    
    #If the guess is not valid, return an empty array
    if guess == None or (len(guess) == 0 and len(game) == 0):
        return []
    
    #If the guess is not valid, return an empty array
    if len(guess) != len(game):
        return []
    
    #Return an empty array
    if len(guess) == 0:
        return []
    
    #Compare each element, if match, return an array of 0s
    if guess == game:
        return [0]*len(guess)
    
    #Return an array of abs(guess - score) for each element
    return [abs(x - y) for (x, y) in zip(guess, game)]
   
