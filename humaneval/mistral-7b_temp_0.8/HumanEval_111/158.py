
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

    words = test.split(' ')
    count = dict()

    for letter in words:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # Return dictionary with the most repeated letter and corresponding count
    return sorted(count.items(), key=lambda x: x[1], reverse=True)
