
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
    # test = map(lambda i: i.replace(" ", ""), test.split())
    # result = test[0]
    # for letter in test[1:]:
    #     if result.count(letter) == test.count(letter):
    #         result += letter
    #     else:
    #         pass
    # return result.count(letter)
    result = {}
    for t in test.split():
        if t not in result:
            result[t] = 0
        result[t] += 1
    return result

