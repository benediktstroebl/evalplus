
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
    n = len(game)
    guess_diff = [0] * n
    guess_diff[0] = guess[0] - game[0]
    for i in range(1, n):
        guess_diff[i] = guess[i] - game[i]
    for i in range(1, n):
        if guess_diff[i] != 0:
            break
    for i in range(n-1,-1,-1):
        guess_diff[i] = guess_diff[i+1]
    for i in range(n-2,-2,-2):
        guess_diff[i] = guess_diff[i+2]
    guess_diff[-1] = guess_diff[-2]
    guess_diff[-2] = guess_diff[-3]
    guess_diff[-3] = guess_diff[-4]
    guess_diff[-4] = guess_diff[-5]
    return guess_diff