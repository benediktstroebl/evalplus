
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
    # Create dictionary for the most frequent letter
    most_frequent_letter_count = {}
    # Loop through each letter in the string
    for letter in test:
        # Check if the letter is in the dictionary
        if letter not in most_frequent_letter_count:
            # If not, add the letter and count
            most_frequent_letter_count[letter] = 1
        # Otherwise, increment the count for that letter
        else:
            most_frequent_letter_count[letter] += 1
    # Sort the dictionary by the counts in descending order
    sorted_most_frequent_letter_count = sorted(most_frequent_letter_count.items(), key=lambda x: x[1], reverse=True)
    # Create a list of the most frequent letters
    most_frequent_letters = [letter for letter, count in sorted_most_frequent_letter_count]
    # Return the dictionary of the most frequent letters and counts
    return dict(most_frequent_letters)
