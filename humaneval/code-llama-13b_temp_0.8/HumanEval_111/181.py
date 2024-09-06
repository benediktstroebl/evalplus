
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
    if test == '':
        return {}
    
    # split the string into a list
    lst = test.split(' ')
    # create a dictionary
    result = {}
    
    # Loop through the list
    for i in lst:
        # check if the key exists in the dictionary
        if result.get(i):
            # increase the count by 1
            result[i] = result.get(i) + 1
        # if key is not found, set the value of the key to 1
        else:
            result[i] = 1
            
    # initialize a variable to keep the max value
    max_value = max(result.values())
    # initialize a list to keep all the keys with the maximum value
    max_value_keys = [key for key in result if result[key] == max_value]
    # return a dictionary with the maximum value and its keys
    return {key: max_value for key in max_value_keys}
    
