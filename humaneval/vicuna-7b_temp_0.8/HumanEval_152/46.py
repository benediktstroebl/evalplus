
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
    score_indx = 0
    guess_indx = 0
    diff = 0
    guess = [int(guess) for guess in guess.split(",")]
    score = [int(i) for i in game.split(",")]
    while score_indx < len(score) and guess_indx < len(guess):
        if score[score_indx] > guess[guess_indx]:
            diff = max(diff, score[score_indx] - guess[guess_indx])
            guess_indx += 1
        elif score[score_indx] < guess[guess_indx]:
            diff = max(diff, guess[guess_indx] - score[score_indx])
            score_indx += 1
        else:
            break
    return [diff if guess_indx < len(guess) else max(0, score[score_indx] - guess[guess_indx]) for score_indx, guess_indx in zip(score, guess)]