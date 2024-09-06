
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
    # sort the input string so that frequent letters come first
    test = sorted(test.lower())
    
    # keep track of the most frequent letter
    count = {}
    max_freq = 0
    
    # iterate over the sorted input string
    for i in range(len(test)):
        # check if the current letter is in the count dictionary
        if i in count:
            # update the count for the current letter
            count[i] += 1
        else:
            # if the current letter is not in the count dictionary,
            # add it with a count of 1
            count[test[i]] = 1
            # update the max_freq if the current letter is more frequent
            if count[test[i]] > max_freq:
                max_freq = count[test[i]]
    
    # return the most frequent letter and its count
    return max_freq, count
