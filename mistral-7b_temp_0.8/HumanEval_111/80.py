
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

    # Separate the letters and the numbers
    l = test.split()
    l_new = [x for x in l if x != '']
    # If there are no letters
    if len(l_new) == 0:
        return {}

    # Create a dictionary
    d = dict.fromkeys(l_new, 0)
    for i in l_new:
        # Add 1 to the dictionary for each letter
        d[i] += 1
    # Return the dictionary
    return d


