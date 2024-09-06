
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
    score_1 = np.array(game)
    guess_1 = np.array(guess)
    guess_2 = np.array(guess)
    for i in range(len(score_1)):
        if guess_1[i] == guess_2[i]:
            diff = abs(score_1[i]-guess_1[i])
            score_1[i] = guess_1[i]
            guess_1[i] = guess_2[i]
            guess_2[i] = diff
            return guess_1, guess_2
    return guess_1, guess_2