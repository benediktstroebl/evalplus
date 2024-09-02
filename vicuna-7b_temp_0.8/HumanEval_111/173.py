
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
    # remove whitespaces
    test = test.upper().replace(" ", "").split()

    # initialize dictionary with frequency of each letter
    freq = {}
    for word in test:
        freq[word] = freq.get(word, 0) + 1

    # sort frequency dictionary
    freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # initialize dictionary to return
    result = {}
    for i, word in enumerate(freq_sorted):
        if i == len(freq_sorted) - 1:
            result[word] = 1
        else:
            result[word] = freq_sorted[i+1][0] + 1

    return result
