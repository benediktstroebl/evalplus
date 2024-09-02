
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
    # write your code here
    # initialize with all values set to infinity
    diff = [float('inf') for i in range(len(game))]
    for i in range(len(game)):
        diff[i] = abs(game[i] - guess[i])
    # sort the guesses in ascending order
    guess_sorted = sorted(guess, reverse=True)
    # iterate over the sorted guesses
    for i in range(len(guess_sorted)):
        j = i
        while diff[j] != float('inf') and j < len(game):
            j += 1
        if j == len(game):
            diff[i] = 0
        else:
            diff[i] = diff[j]
    return diff
