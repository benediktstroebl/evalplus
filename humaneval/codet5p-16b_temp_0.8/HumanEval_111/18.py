
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

    test = test.replace(' ', '')
    test = test.lower()
    counts = dict()
    for letter in test:
        if counts.get(letter) == None:
            counts[letter] = 1
        else:
            counts[letter] += 1
    maxcount = 0
    letters = []
    for letter in counts.keys():
        if counts[letter] > maxcount:
            letters = []
            maxcount = counts[letter]
            letters.append(letter)
        elif counts[letter] == maxcount:
            letters.append(letter)
        else:
            pass

    return {letter: counts[letter] for letter in letters}
