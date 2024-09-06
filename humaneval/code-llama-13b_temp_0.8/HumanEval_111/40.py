
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
    if test == "":
        return {}
    test_dict = {}
    list_of_letters = []
    for i in test.split(" "):
        if i not in test_dict:
            test_dict[i] = 1
        else:
            test_dict[i] += 1
        if i not in list_of_letters:
            list_of_letters.append(i)
    max_value = max(test_dict.values())
    return {letter: max_value for letter in list_of_letters if test_dict[letter] == max_value}
