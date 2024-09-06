
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
    # Convert the string to a list of characters
    char_list = list(set(test))
    # Create an empty dictionary to store the counts
    counts = {}
    # Loop through the characters in the list
    for char in char_list:
        # If the character is not in the dictionary, add it with a count of 1
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    # Sort the dictionary by the count of each character
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    # Return the dictionary with the most frequent character and its count
    return sorted_counts[0][0]

test = input("Enter a space separated string: ")
