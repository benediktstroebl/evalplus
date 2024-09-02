
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

    if test == "":
        return {}
    else:
        test = test.split()
        word = test[0]
        letters = []
        dict = {}
        for i in range(0,len(word)):
            letters.append(word[i])
        for x in range(0, len(letters)):
            for y in range(0, len(test)):
                if letters[x] in test[y]:
                    dict.update({letters[x]: test.count(letters[x])})
        return dict
