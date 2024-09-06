
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
    letters_dict = {}
    for i in test.split():
        if i in letters_dict:
            letters_dict[i] += 1
        else:
            letters_dict[i] = 1
    if len(letters_dict) == 1:
        return {k: v for k, v in letters_dict.items()}
    else:
        return {k: v for k, v in sorted(letters_dict.items(), key=lambda item: item[1], reverse=True)}


