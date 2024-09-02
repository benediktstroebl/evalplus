
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
    d = {}
    word = test.split()
    for char in word:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    max_count = 0
    max_char = []
    for char in d:
        if d[char] > max_count:
            max_count = d[char]
            max_char = [char]
        elif d[char] == max_count:
            max_char.append(char)
    return dict((char, max_count) for char in max_char)

