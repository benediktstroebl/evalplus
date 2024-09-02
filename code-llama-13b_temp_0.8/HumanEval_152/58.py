
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
    
    
    #function to compare the guesses and the actual result
    #a function is used to make it testable and reusable
    def compareScore(game,guess):
        if len(game)==len(guess):
            #loop through both arrays and compare the values of the index
            for i in range(0,len(game)):
                #if the guessed value is the same as the actual value
                if guess[i]==game[i]:
                    #append a 0 to the result array
                    result.append(0)
                else:
                    #if not 0, append the difference between the guessed value and the actual value
                    result.append(abs(guess[i]-game[i]))
            #return the result array
            return result
        else:
            #if the length of the arrays are not the same, return an empty list
            return []
        
    #initialise an empty list called result
    result = []
    #call the compareScore function to find the result
    result = compareScore(game,guess)
    #return the result
    return result


