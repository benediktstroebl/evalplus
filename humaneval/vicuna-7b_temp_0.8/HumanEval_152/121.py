
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
    score_arr = np.array(game)
    guess_arr = np.array(guess)
    if guess_arr.size != score_arr.size:
        return [0,0,0,0,0,0]
    else:
        correct = 0
        for i in range(score_arr.size):
            if score_arr[i] == guess_arr[i]:
                correct += 1
            elif guess_arr[i] > 0 and score_arr[i] > guess_arr[i]:
                diff = abs(score_arr[i] - guess_arr[i])
                return [diff,diff,diff,diff,diff,diff]
            elif guess_arr[i] < 0 and score_arr[i] < guess_arr[i]:
                diff = abs(score_arr[i] - guess_arr[i])
                return [-diff,-diff,-diff,-diff,-diff,-diff]
            else:
                return [0,0,0,0,0,0]