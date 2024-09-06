
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
    # check that the number of elements in the arrays match
    assert len(game) == len(guess), f"Length of arrays do not match: {game} vs {guess}"
    # sort the elements in both arrays
    game = sorted(game)
    guess = sorted(guess)
    # initialize a list to store the results
    results = [0] * len(game)
    # loop through the elements of the arrays and check if the guess is correct
    for i in range(len(game)):
        if guess[i] == game[i]:
            results[i] = 0
        else:
            difference = abs(guess[i] - game[i])
            results[i] = difference
    return results

