
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
    buckets = {}
    last_char = None
    for i, char in enumerate(test):
        if char != last_char:
            if last_char is not None:
                buckets[last_char] = (buckets[last_char][0], i - 1)
            last_char = char
    if last_char is not None:
        buckets[last_char] = (buckets[last_char][0], i)
    return buckets

