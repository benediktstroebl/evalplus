
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
    #your code here

    result = [0] * len(game)
    for i in range(len(game)):
        result[i] = abs(game[i] - guess[i])
    return result


    """
    Given the scores of players A and B in a series of matches,
    return a list of which player won each match and which player lost each match.
    It is guaranteed that one player won each match.
    """

    def scores(A, B):
        """
        A and B are lists of integers representing the scores of players A and B
        in a series of matches, in the order in which the matches were played.
        """
        # Your code here
        result = [None] * len(A)
        for i in range(len(A)):
            if A[i] > B[i]:
                result[i] = "A"
            elif A[i] < B[i]:
                result[i] = "B"
            else:
                result[i] = "D"
        return result

    """
