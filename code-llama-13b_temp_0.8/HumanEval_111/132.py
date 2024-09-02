
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
    test_dict = {}
    for letter in test.split():
        if letter in test_dict:
            test_dict[letter] += 1
        else:
            test_dict[letter] = 1
    sorted_dict = sorted(test_dict.items(), key=lambda k: k[1], reverse=True)
    for item in sorted_dict:
        if item[1] == sorted_dict[0][1]:
            print(item[0], item[1])
        else:
            break

