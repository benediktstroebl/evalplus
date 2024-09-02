
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
    #A.C
    #numpy speed up
    from numpy import convolve
    out = np.convolve(game,guess)
    counts = np.array([out[i] != game[i] for i in range(len(out))])
    return counts 
    """
    
    """
    #B.C
    #I should also compare scores, but why not.
    #lots of similar enough scores
    out = [guess[i] - game[i] for i in range(len(guess))]
    return out
    """
    
    """
    #C.C
    #Possible speed up
    #how much faster?
    #time test
    from timeit import timeit
    #A
    start = timeit()
    compare(game,guess)
    end = timeit()
    print end - start
    #B
    start = timeit()
    compare_2(game,guess)
    end = timeit()
    print end - start
    #C
    start = timeit()
    compare_3(game,guess)
    end = timeit()
    print end - start
    """
    """
    #D.C
    #I believe it takes forever on my machine
    #cannot even do it
    from timeit import timeit
    #A
    start = timeit()
    compare(game,guess)
    end = timeit()
    print end - start
    #B
    start = timeit()
    compare_2(game,guess)
    end = timeit()
    print end - start
    #C
    start = timeit()
    compare_3(game,guess)
    end = timeit()
    print end - start
    """
    
    
    #a.c
    #I should have compared scores instead of guessing. Then I wouldn't need to compare scores.
    #instead I can use the sum of the array (w/ absolute value) to compare
    #guesses and scores
    #now I can find the absolute value of the differences between scores and guesses.
    