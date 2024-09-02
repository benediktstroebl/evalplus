
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
    # Create an empty dictionary to store the results
    results = {}
    
    # Loop through the characters in the string
    for c in test:
        # If the character is a letter, check if it has already been seen
        if c.isalpha():
            if c in results:
                results[c] += 1
            else:
                results[c] = 1
    
    # Sort the results by occurrence in descending order
    results = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
    
    # Return the results
    return results
