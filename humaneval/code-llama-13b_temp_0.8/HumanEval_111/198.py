
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
    print(test)
    result = {}
    test_list = test.split(" ")
    for letter in test_list:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    
    # Get most repeated letter(s)
    most_repeated = max(result.values())
    # Get the letter with most repeated
    most_repeated_letter = [k for k,v in result.items() if v == most_repeated]
    # Get only the letters with most repeated
    result = {k:result[k] for k in most_repeated_letter}
    
    print(result)
    return result
