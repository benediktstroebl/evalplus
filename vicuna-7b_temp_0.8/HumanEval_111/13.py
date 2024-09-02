
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
    # convert string to list of characters
    chars = list(set(test))
    # count occurrence of each character
    counts = {}
    for char in chars:
        counts[char] = counts.get(char, 0) + 1
    # sort characters by occurrence
    sorted_chars = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    # return dictionary of characters and their count
    return dict(sorted_chars)

test = input("Enter a string representing a space separated lowercase letters: ")
