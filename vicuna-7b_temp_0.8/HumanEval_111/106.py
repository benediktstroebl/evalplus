
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
    # Define a counter for each letter in the alphabet
    counters = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        counters[letter] = 0
    for char in test:
        if char in counters:
            counters[char] += 1
        else:
            counters[chr(ord(char) + 1)] += 1
    # Sort the keys by frequency and return the most frequent letter
    sorted_counters = sorted(counters.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_counters)
