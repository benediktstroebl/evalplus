
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
    # Split the string on whitespace and convert to lowercase
    words = test.split()
    words = [word.lower() for word in words]
    
    # Initialize a dictionary to store the counts of each letter
    counts = {}
    
    # Iterate over the words
    for word in words:
        # If the word is in the dictionary, increment the count
        if word in counts:
            counts[word] += 1
        else:
            # If the word is not in the dictionary, add it with a count of 1
            counts[word] = 1
    
    # Return the dictionary of counts
    return counts
