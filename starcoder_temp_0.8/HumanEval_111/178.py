
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
    letters = test.split()
    dict = {}
    for i in range(len(letters)):
        if letters[i] in dict:
            dict[letters[i]] += 1
        else:
            dict[letters[i]] = 1
    maximum = max(dict.values())
    max_key = [k for k in dict.keys() if dict[k] == maximum]
    return dict

