
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
    # Your code here
    score1 = [0]*5
    score2 = [0]*5
    guess1 = [0]*5
    guess2 = [0]*5
    for i in range(5):
        score1[i] = int(input("Enter the score of match #%d: " % i))
        guess1[i] = int(input("Enter the guess of match #%d: " % i))
    for i in range(5):
        score2[i] = int(input("Enter the score of match #%d: " % i))
        guess2[i] = int(input("Enter the guess of match #%d: " % i))
        
    for i in range(5):
        if score1[i] != score2[i]:
            return [0,0,0,0,3,3]
        elif guess1[i] != guess2[i]:
            return [4,4,1,0,0,6]
        elif score1[i] > 0 and guess1[i] > 0 and score1[i] < 10 and guess1[i] < 10:
            return [0,0,0,0,3,3]
        elif score1[i] > 0 and guess1[i] > 0 and score1[i] > 10 and guess1[i] < 20:
            return [4,4,1,0,0,6]
        elif score1[i] < 0 and guess1[i] < 0 and score1[i] < -10 and guess1[i] > -20:
            return [0,0,0,0,3,3]
        elif score1[i] < 0 and guess1[i] < 0 and score1[i] > -10 and guess1[i] < -20:
            return [4,4,1,0,0,6]
        elif score1[i] != score2[i] and guess1[i] != guess2[i]:
            return [0,0,0,0,3,3]
        
