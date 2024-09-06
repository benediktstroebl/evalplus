
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
    # Make a dictionary of the input string, counting the frequency of each letter
    freq = {}
    for letter in test:
        if letter.lower() in freq:
            freq[letter.lower()] += 1
        else:
            freq[letter.lower()] = 1

    # Find the most common letter and its count
    max_count = max(freq.values())
    max_letter = list(freq.keys())[0]

    # If there is only one letter, return a dictionary with that letter and its count
    if max_count == 1:
        return {max_letter: max_count}
    else:
        return {max_letter: max_count}
