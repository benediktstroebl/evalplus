
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

    # You can use this code as an example:
    # from collections import defaultdict
    # from string import ascii_lowercase as letters
    # d = defaultdict(int)
    # for letter in test:
    #     if letter in letters:
    #         d[letter] += 1
    # return dict(d)

    # Here are your previous test cases to see if you've passed them:
    # print(histogram('a b c'))  # == {'a': 1, 'b': 1, 'c': 1}
    # print(histogram('a b b a'))  # == {'a': 2, 'b': 2}
    # print(histogram('a b c a b'))  # == {'a': 2, 'b': 2}
    # print(histogram('b b b b a'))  # == {'b': 4}
    # print(histogram(''))  # == {}

    d = {}
    for letter in test:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    return d
