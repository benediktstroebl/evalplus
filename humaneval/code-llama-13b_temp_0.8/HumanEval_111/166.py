
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
    dct = {}
    for char in test:
        dct[char] = dct.get(char, 0) + 1
    sorted_dct = sorted(dct.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_dct)
    count = sorted_dct[0][1]
    ans = {key: value for key, value in sorted_dct if value == count}
    return ans

