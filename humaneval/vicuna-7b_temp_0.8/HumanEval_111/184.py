
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
    letters = set(test)
    letter_counts = {}
    
    # Find the most common letter
    for letter in letters:
        count = letters.count(letter)
        if count > letter_counts.get(letter, 0):
            letter_counts[letter] = count + 1
            if letter != test[0]:
                letter_counts[letter] -= letter_counts.get(test[0], 0)
    
    return letter_counts