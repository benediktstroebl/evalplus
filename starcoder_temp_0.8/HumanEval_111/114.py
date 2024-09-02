
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
    
    list = []
    dictionary = {}

    for c in test.split():
        list.append(c)

    for word in list:
        if word in dictionary:
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = 1

    max = 0
    for key, value in dictionary.items():
        if value > max:
            max = value
            words = [key]
        elif value == max:
            words.append(key)

    if len(words) == 1:
        return {words[0]: max}
    else:
        return {words[0]: max, words[1]: max}
