
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
    word_dict = {}
    if test == '':
        return {}
    else:
        for letters in test.split():
            if letters in word_dict.keys():
                word_dict[letters] += 1
            else:
                word_dict[letters] = 1
    max_count = max(word_dict.values())
    for letters in word_dict.keys():
        if word_dict[letters] == max_count:
            return {letters:word_dict[letters]}
        else:
            return word_dict

