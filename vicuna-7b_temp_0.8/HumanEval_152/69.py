
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
    scores = [int(s) for s in game]
    guesses = [int(g) for g in guess]
    correct = 0
    for i in range(0,len(scores),2):
        if guesses[i] == scores[i]:
            correct +=1
        else:
            diff = abs(guesses[i]-scores[i])
            if guesses[i] > scores[i]:
                diff = -diff
            return [diff if j==i else 0 for j in range(len(guesses)) if j!=i]
    return [diff if i==len(scores) -1 else 0 for i in range(len(guesses))]

input = [int(s) for s in sys.stdin.read().strip().split()]
game = input[1:]
guess = input[1:]
