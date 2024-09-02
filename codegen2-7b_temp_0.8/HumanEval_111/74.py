
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
    if test == "":
        return {}
    occurences = {}
    for letter in test:
        if letter in occurences:
            occurences[letter] += 1
        else:
            occurences[letter] = 1
    most_occurrences = sorted(occurences.items(), key = lambda x: x[1], reverse = True)
    return most_occurrences[0
