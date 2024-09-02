
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
    letter_dict = {}
    for letter in test.split(" "):
        letter_dict[letter] = letter_dict.get(letter, 0) + 1

    most_occur_letter = None
    max_occur = 0
    for letter, occur in letter_dict.items():
        if occur > max_occur:
            most_occur_letter = letter
            max_occur = occur
    return {most_occur_letter: max_occur}
