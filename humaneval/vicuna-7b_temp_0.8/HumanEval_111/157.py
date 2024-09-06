
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
    # sort the string
    sorted_string = sorted(test.lower())
    # remove any non-alphanumeric characters
    sorted_string = [c for c in sorted_string if c.isalnum()]
    # get the length of the string
    n = len(sorted_string)
    # initialize a dictionary to store the count of each letter
    count = {}
    # for each letter in the string
    for i in range(n):
        # if the current letter is not in the dictionary
        if i not in count:
            # increment the count of the current letter
            count[i] = 1
        else:
            # increment the count of the current letter
            count[i] += 1
    # return the dictionary of counts
    return count
