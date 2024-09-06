
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    #This function returns a dictonary of the letter with the most repetition and containing the corresponding count.
    #It will return a dict of {letter:number_of_times_letter_occurs}
    #Create a dictionary for the keys.
    keys = {}
    for x in test.split():
        keys[x] = keys.get(x,0) + 1
        #If the key doesn't exist, set the value to 0.
        #If it does, just add 1 to the value.
    return keys
