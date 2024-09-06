
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
    scores = [0, 2, 3, 4, 5, 1]
    guesses = [1, 2, 3, 4, 2, -2]
    my_result = compare(scores,guesses)

    # def get_absolute(x,y):
    #     if x<y:
    #         return y-x
    #     else:
    #         return x-y
    #
    # result = []
    # for i in range(len(guesses)):
    #     result.append(get_absolute(scores[i],guesses[i]))
    # return result
    #
    # # #
    #
    # for i in range(len(guesses)):
    #     if scores[i]==guesses[i]:
    #         result[i]=0
    #     else:
    #         result[i]=scores[i]-guesses[i]
    # return result
    #
    #
    #
    #
    #
    # return result
