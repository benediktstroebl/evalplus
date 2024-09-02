
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
    histogram = {}
    for letter in test.split():
        if letter in histogram.keys():
            histogram[letter] += 1
        else:
            histogram[letter] = 1
    max_repetition = max(histogram.values())
    max_repetition_letters = []
    for key, value in histogram.items():
        if value == max_repetition:
            max_repetition_letters.append(key)
    return {x:histogram[x] for x in max_repetition_letters}
