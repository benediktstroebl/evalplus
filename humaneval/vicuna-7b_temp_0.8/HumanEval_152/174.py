
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
    def f(x,y):
        if y[0] != x[0]:
            return 1
        elif y[1] != x[1]:
            return 1
        else:
            return abs(y[2]-x[2])
    scores1 = game[0]
    scores2 = game[1]
    guess1 = guess
    guess2 = game[2]
    diffs = [f(scores1,score) for score in scores2]
    guess_diffs = [f(guess1,guess2)]
    return guess_diffs + diffs