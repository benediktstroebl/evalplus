
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
    dictionary = {}
    for i in range(len(test)):
        if test[i] in dictionary:
            dictionary[test[i]] += 1
        else:
            dictionary[test[i]] = 1

    max_rep = dictionary[test[0]]
    final = {}
    for k in dictionary:
        if dictionary[k] == max_rep:
            final[k] = dictionary[k]
        elif dictionary[k] > max_rep:
            final.clear()
            max_rep = dictionary[k]
            final[k] = dictionary[k]
    return final
    
