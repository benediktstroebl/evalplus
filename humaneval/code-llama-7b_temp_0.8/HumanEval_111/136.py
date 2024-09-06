
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

    counter = {}
    counter_1 = {}
    split_string = test.split()

    for i in split_string:
        counter[i] = split_string.count(i)
        counter_1[i] = split_string.count(i)
        if counter_1[i] > 1:
            counter_1[i] = split_string.count(i)
        else:
            counter_1[i] = split_string.count(i)

    return counter_1

