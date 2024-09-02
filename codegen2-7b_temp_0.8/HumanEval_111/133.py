
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
    a = test.split()
    a_count = {}
    for elem in a:
        if elem in a_count:
            a_count[elem] += 1
        else:
            a_count[elem] = 1
    max_count = 0
    max_elem = ""
    for elem in a_count:
        if a_count[elem] > max_count:
            max_count = a_count[elem]
            max_elem = elem
    return max_elem, max_count

