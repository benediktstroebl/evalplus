
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
    max_value = 0
    max_letter = None
    letter_count = dict()

    for i in test.split():
        if i in letter_count:
            letter_count[i] += 1
        else:
            letter_count[i] = 1

        if letter_count[i] > max_value:
            max_value = letter_count[i]
            max_letter = i
    return {max_letter: max_value}
