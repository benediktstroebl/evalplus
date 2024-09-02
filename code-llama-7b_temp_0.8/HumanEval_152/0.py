
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


    """
    Let's think about how we can solve this. 
    
    I'm thinking that we need to take the scores and guesses, and compare them.
    We need to find the absolute difference between the scores and the guesses.
    We know that the length of these arrays is going to be the same, so we can use that
    as our base condition for the for loop.
    
    I'm thinking that we will need a function, which will take the difference of
    the two variables. We will then return that difference.
    
    """

    # implement the code to create an array of differences between the guesses and scores
    # then return the array of differences

    differences = []
    for i in range(len(game)):
        diff = abs(game[i] - guess[i])
        differences.append(diff)
    return differences

