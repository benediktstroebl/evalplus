
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
    #convert string to lowercase and split into list
    words = test.lower().split()
    #create empty dictionary to store count of each letter
    word_count = {}
    #iterate through the list of words
    for word in words:
        #if the word is not in the dictionary, add it with a count of 1
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    #return the dictionary of most frequent letters and their count
    return word_count