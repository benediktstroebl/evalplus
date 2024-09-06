
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
    scores=game
    guesses=guess
    scores_without_zero=[[int(i) for i in s.split()) if i != '0' and i >= 0] for s in scores
    guesses_without_zero=[[int(i) for i in s.split()) if i != '0' and i >= 0] for s in guesses
    correct=0
    for i in range(len(scores_without_zero)):
        if scores_without_zero[i] == guesses_without_zero[i]:
            correct +=1
        else:
            diff=abs(scores_without_zero[i]-guesses[i])
            return [diff if i==len(scores_without_zero)-1 else diff+1 if scores_without_zero[i] > guesses[i] else diff-1 if scores_without_zero[i] < guesses[i] else diff for i in range(len(scores_without_zero))]
    return [diff for i in range(len(scores_without_zero))]