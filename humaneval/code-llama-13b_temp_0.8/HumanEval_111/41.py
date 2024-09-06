
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
    
    #return test
    
    #test.split()
    #print(test)
    
    #result = {}
    #max_count = 0
    #for i in test.split():
    #    if i in result:
    #        result[i] += 1
    #    else:
    #        result[i] = 1
    #    if result[i] > max_count:
    #        max_count = result[i]
    #return { key: value for key, value in result.items() if value == max_count }
    
    return { key: value for key, value in collections.Counter(test.split()).most_common() }
