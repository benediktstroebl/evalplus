
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
    
    lst = test.split()
    lettercount = {}
    
    for word in lst:
        for letter in word:
            if letter in lettercount:
                lettercount[letter] += 1
            else:
                lettercount[letter] = 1
    
    m = max(lettercount.values())
    ret = []
    
    for letter, count in lettercount.items():
        if count == m:
            ret.append(letter)
    
    return lettercount
