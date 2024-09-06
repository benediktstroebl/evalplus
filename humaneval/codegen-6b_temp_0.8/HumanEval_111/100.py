
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
    # for each char, if its not in the map, add it with 1, else add one to the count
    # when the loop ends, return a dict with the letter and count
    
    if test == '':
        return {}
    
    hist = {} 
    for char in test:
        if char not in hist:
            hist[char] = 1
        else:
            hist[char] += 1
    
    return hist
        
    # my idea - make a list of char, count pair, return the max
    # collect = []
    # hist = {}
    # for char in test:
    #     collect.append([char, test.count(char)])
    # for pair in collect:
    #     if pair[1] not in hist:
    #         hist[pair[1]] = 1
    #     else:
    #         hist[pair[1]] += 1
    # return hist