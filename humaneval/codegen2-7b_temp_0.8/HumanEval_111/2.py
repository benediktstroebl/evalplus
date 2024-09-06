
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
    
    def add_count(dictionary):
        if dictionary == {}:
            return dictionary
        else:
            temp = dictionary.keys()
            value = dictionary.values()
            count = value[0]
            if count in temp:
                temp.remove(count)
                dictionary[count] = value[0] + 1
            return dictionary
    
    return add_count(Counter(test.split(' ')))

