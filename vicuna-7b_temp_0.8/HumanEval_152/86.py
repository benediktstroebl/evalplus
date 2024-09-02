
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
    # Convert all scores to be positive integers
    scores = [int(i) for i in game]
    guess = [int(i) for i in guess]
    
    # Find the index of the last correct guess
    correct_guesses = 0
    for i in range(len(scores)):
        if guess[correct_guesses] == scores[correct_guesses]:
            correct_guesses += 1
        else:
            break
    
    # Initialize a list to store the differences
    differences = [0] * len(scores)
    
    # Loop through the remaining guesses
    for i in range(correct_guesses, len(scores)):
        # Subtract the correct guess from the current guess
        difference = abs(guess[i] - scores[i])
        differences[i] = difference
    
    return differences
