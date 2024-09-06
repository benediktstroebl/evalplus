
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
    #We can use dictionary's setdefault function to do this
    histogram = {}

    # split the string into a list of words
    words = test.split()

    for word in words:
        # If the word is not in the histogram, add it with a count of 1
        if word not in histogram:
            histogram[word] = 1
        # If the word is in the histogram, increment the count for that word
        else:
            histogram[word] += 1

    return histogram

