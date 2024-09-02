
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
    freq = {}
    for s in test.split():
        if s in freq:
            freq[s] += 1
        else:
            freq[s] = 1

    max_freq = 0
    max_freq_strs = {}

    for s in freq.keys():
        if freq[s] == max_freq:
            max_freq_strs[s] = freq[s]
        elif freq[s] > max_freq:
            max_freq_strs = {s: freq[s]}
            max_freq = freq[s]

    return max_freq_strs

