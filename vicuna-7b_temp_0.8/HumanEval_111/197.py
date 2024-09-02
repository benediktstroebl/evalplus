
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
    # convert string to lowercase, split it into a list, convert each letter to lowercase and
    # count the number of occurrences of each letter
    count = {}
    for letter in test.lower().split():
        count[letter] = count.get(letter, 0) + 1
    max_letter = max(count, key=count.get)
    return count[max_letter]
