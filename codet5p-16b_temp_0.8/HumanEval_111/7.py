
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

    
    test = test.lower() #turn all the characters to lowercase
    test = test.split() #split the string into a list of words
    histogram = {} #create a dictionary
    
    for word in test:
        if word in histogram:
            histogram[word] += 1 #increment the counter if the word is already in the histogram
        else:
            histogram[word] = 1 #add the word to the histogram
    
    histogram_max = max(histogram.values()) #find the maximum number of the values
    
    for word in histogram:
        if histogram[word] == histogram_max: #if the maximum number is found, return all of them
            return histogram
            
    return histogram

