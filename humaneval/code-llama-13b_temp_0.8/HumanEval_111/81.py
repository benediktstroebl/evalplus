
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
    if test == '':
        return {}
    else:
        words = test.split()
        dictionary = {}
        for word in words:
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1

        largest_number = max(dictionary.values())
        largest_number_list = []
        for k, v in dictionary.items():
            if v == largest_number:
                largest_number_list.append(k)
        return {k: v for k, v in dictionary.items() if v == largest_number}
