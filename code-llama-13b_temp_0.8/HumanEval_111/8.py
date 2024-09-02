
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
    dict = {}
    if test == "":
        return {}
    else:
        test = test.split()
        for letter in test:
            if letter in dict.keys():
                dict[letter] += 1
            else:
                dict[letter] = 1
        
        max = 0
        for value in dict.values():
            if value >= max:
                max = value
        max_list = []
        for key, value in dict.items():
            if value == max:
                max_list.append(key)
        final = {}
        for letter in max_list:
            final[letter] = dict[letter]
        return final
