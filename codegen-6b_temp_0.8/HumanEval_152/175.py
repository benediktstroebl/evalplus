
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
    scores = list(map(int,game))
    guess = list(map(int,guess))
    i = 0
    j = 0
    guess_counter = 0
    score_counter = 0
    output = []
    while i < len(scores) and j < len(guess):
        if guess_counter < score_counter:
            j += 1
        elif score_counter < guess_counter:
            i += 1
        elif scores[i] == guess[j]:
            i += 1
            j += 1
            score_counter += 1
        else:
            len_diff = abs(guess[j] - scores[i])
            output.append(len_diff)
            score_counter += 1
            i += 1
            j += 1
    while i < len(scores):
        output.append(0)
        i += 1
    while j < len(guess):
        output.append(0)
        j += 1
    return output

for i,(a,b) in enumerate(zip(game,guess)):
    if a == b:
        print(0)
    else:
        print(abs(a-b))









