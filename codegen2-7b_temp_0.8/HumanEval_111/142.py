
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
    words = test.strip().split(' ')
    d = {}
    for i in range(len(words)):
        word = words[i]
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    
    for key in d:
        print(key, d[key])
