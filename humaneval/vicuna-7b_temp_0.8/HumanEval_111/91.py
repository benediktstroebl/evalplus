
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
    # convert to lowercase and remove whitespaces
    s = s.lower().split()
    
    # initialize dictionary to store the letter and its count
    count = {}
    
    # loop through the string and increment the count for each letter
    for x in s:
        count[x] = count.get(x, 0) + 1
    
    # update the count for each letter in the dictionary
    for key, value in count.items():
        count[key] = value
    
    # return the dictionary of the most frequent letter and its count
    return count
