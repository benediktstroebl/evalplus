
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
    # Remove all spaces
    test = test.strip().lower()
    # Convert to set
    test_set = set(test)
    # Get the most repeated letter and its count
    most_repeated = max(test_set, key=test_set.count)
    count = test_set.count(most_repeated)
    # Get all the letters that appear more than once
    letter_set = set(test_set)
    for letter in letter_set - {most_repeated}:
        count -= 1
        if count == 0:
            del letter_set[letter_set.index(letter)]
    return {''.join(sorted(letter_set)): count}
