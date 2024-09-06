
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

    # return a dict with key being the word and value being the number of times it appears
    output_dict = {}
    for word in test.split():
        output_dict[word] = output_dict.get(word, 0) + 1
    most_occur = max(output_dict.values())
    result_dict = {}
    for word, occur in output_dict.items():
        if occur == most_occur:
            result_dict[word] = occur
    return result_dict
