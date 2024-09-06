
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

    # ====================================================================
    # This is a value of the same length as the number of items in game
    # It will be returned at the end. This value will indicate if the
    # guess was within the value of the game or not.
    # ====================================================================
    result = [0] * len(game)

    # ====================================================================
    # This loop makes sure that we iterate through each item in the list
    # ====================================================================
    for i in range(len(game)):

        # ====================================================================
        # If the guess is equal to the game
        # ====================================================================
        if guess[i] == game[i]:
            # ====================================================================
            # set the result to 0
            # ====================================================================
            result[i] = 0

        # ====================================================================
        # If the guess is not equal to the game
        # ====================================================================
        if guess[i] != game[i]:

            # ====================================================================
            # set the result to the difference of the guess and the game
            # ====================================================================
            result[i] = abs(guess[i] - game[i])

    # ====================================================================
    # return the result list
    # ====================================================================
    return result
