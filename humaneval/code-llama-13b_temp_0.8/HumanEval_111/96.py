
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

    if not isinstance(test, str):
        raise TypeError(f"The argument of the histogram function should be of type str, not {type(test)}")

    dico = {}
    for k in test.split():
        dico[k] = dico.get(k, 0) + 1
    return {k:v for k, v in sorted(dico.items(), key=lambda item: item[1], reverse=True)}
