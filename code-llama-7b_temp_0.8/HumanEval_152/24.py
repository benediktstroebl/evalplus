
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


    #==================================================================
    # method 1: list comprehension
    #==================================================================
    # result = [abs(score-guess) for score,guess in zip(game,guess)]
    # return result

    #==================================================================
    # method 2: zip + list comprehension
    #==================================================================
    # result = [abs(score-guess) for score,guess in zip(game,guess)]
    # return result

    #==================================================================
    # method 3: zip + map
    #==================================================================
    # result = map(abs,zip(game,guess))
    # return list(result)

    #==================================================================
    # method 4: zip + lambda
    #==================================================================
    # return [abs(score-guess) for score,guess in zip(game,guess)]

    #==================================================================
    # method 5: zip + lambda + list comprehension
    #==================================================================
    # return [abs(score-guess) for score,guess in zip(game,guess)]

    #==================================================================
    # method 6: zip + lambda + list comprehension + filter
    #==================================================================
    # return list(filter(None,map(lambda x,y: x+y,game,guess)))

    #==================================================================
    # method 7: zip + lambda + filter
    #==================================================================
    # return list(filter(None,map(lambda x,y: x+y,game,guess)))

    #==================================================================
    # method 8: map + filter
    #==================================================================
    # return list(filter(None,map(lambda x,y: x+y,game,guess)))

    #==================================================================
    # method 9: map + filter + lambda
    #==================================================================
    # return list(filter(lambda x: x>0,map(lambda x,y: x+y,game,guess)))

    #================================================================
