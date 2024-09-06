
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
    # split the string into a list of characters
    chs = test.split()
    ch_count = {}
    
    # count the occurrences of each character
    for char in chs:
        if char in ch_count:
            ch_count[char] += 1
        else:
            ch_count[char] = 1
    
    # return the letter with the most repetition and the corresponding count
    max_count = max(ch_count.values())
    return {char: count for char, count in ch_count.items() if count == max_count}
