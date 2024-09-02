
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
    # Store all unique letters in a set
    unique_letters = set()
    for letter in test:
        if letter.lower() not in unique_letters:
            unique_letters.add(letter.lower())

    # Initialize a dictionary to store the letter-count pairs
    letter_count_pairs = {}

    # Iterate through the unique letters
    for letter in unique_letters:
        # If the count is 1, increment the count and add the letter to the dictionary
        if len(test) == 1 or test.count(letter) == 1:
            letter_count_pairs[letter] = 1
        # If the count is greater than 1, add the letter to the dictionary and increment the count
        else:
            letter_count_pairs[letter] += 1

    return letter_count_pairs
