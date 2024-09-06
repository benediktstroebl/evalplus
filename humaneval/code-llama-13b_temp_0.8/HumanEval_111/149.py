
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
    if not test:
        return {}
    # splits the string in a list of strings and returns the first letter of each word
    test = [x[0] for x in test.split()]
    dic = {}
    # in case there are more letters with the same amount of repetitions
    max_value = 0
    for x in test:
        dic[x] = dic.get(x, 0) + 1
        if max_value < dic[x]:
            max_value = dic[x]
    return {key: value for key, value in dic.items() if value == max_value}
