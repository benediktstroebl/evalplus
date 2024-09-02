
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
    # convert string to lowercase and split into a list of letters
    letters = test.lower().split()
    # count the number of occurrences of each letter
    counts = Counter(letters)
    # get the most frequent letter and its count
    max_val = max(counts.values())
    max_letter = letters[counts[max_val] - 1]
    return max_letter, counts[max_val]
