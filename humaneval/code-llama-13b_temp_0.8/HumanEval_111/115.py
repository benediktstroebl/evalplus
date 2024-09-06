
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

    letters = test.split()
    result = {}

    for letter in letters:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1

    most_common = []
    most_occurance = max(result.values())
    for key, value in result.items():
        if value == most_occurance:
            most_common.append(key)

    final = {}

    for key in most_common:
        final[key] = result[key]

    return final
