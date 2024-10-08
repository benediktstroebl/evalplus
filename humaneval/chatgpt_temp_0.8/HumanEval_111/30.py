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
    
    # Split the string into a list of lowercase letters
    letters = test.lower().split()

    # Create an empty dictionary to store the letter counts
    counts = {}

    # Loop through each letter in the list and count its occurrences
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    # Find the maximum count value
    max_count = max(counts.values())

    # Create a dictionary of letters with the maximum count value
    max_letters = {}
    for letter, count in counts.items():
        if count == max_count:
            max_letters[letter] = count

    return max_letters
