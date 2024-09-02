
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
    dictionary = {}
    if not test:
        return dictionary
    
    split_test = test.split()
    for letter in split_test:
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1
    
    max_occur = 0
    max_letters = []
    for key, value in dictionary.items():
        if value >= max_occur:
            if value > max_occur:
                max_occur = value
                max_letters.clear()
            max_letters.append(key)
    return {key: value for key, value in dictionary.items() if value in max_letters}
    
    
