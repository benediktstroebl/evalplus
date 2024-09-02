
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
        
    test_list = test.split()
    freq_dict = {}
    max_occurrence = 0
    
    for word in test_list:
        freq_dict[word] = test_list.count(word)
    
    for word in test_list:
        if freq_dict[word] > max_occurrence:
            max_occurrence = freq_dict[word]
    
    final_dict = {}
    
    for k, v in freq_dict.items():
        if v == max_occurrence:
            final_dict[k] = v
    return final_dict
