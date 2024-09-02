
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
    
    # split test string by space, store list
    text = test.split(' ')
    # create dictionary with letter and count
    d = {word: text.count(word) for word in text}
    # find max value in dict
    max_value = max(d.values())
    # create new dictionary with max values
    final_dict = {k: v for k, v in d.items() if v == max_value}

    return final_dict
