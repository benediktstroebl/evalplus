
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
    try:
        histogram_dict = {}
        test_split = test.split()
        for char in test_split:
            if char not in histogram_dict:
                histogram_dict[char] = 1
            else:
                histogram_dict[char] = histogram_dict[char] + 1
        
        return histogram_dict
    except ValueError:
        print(ValueError)
        return histogram(test)

