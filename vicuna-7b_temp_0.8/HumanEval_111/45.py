
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
    # Create a default dictionary with all letters as keys and their count as values
    counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
              'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
              'y': 0, 'z': 0}
    
    # Split the input string into a list of characters
    words = test.split()
    
    # Loop through each character in the list
    for word in words:
        # Add the count for the current word to the counts dictionary
        counts[word] += 1
    
    # Sort the counts dictionary by the count value, in descending order
    counts.sort(reverse=True)
    
    # Create a dictionary with the most frequent letter as the key and its count as the value
    result = {}
    for count, letter in counts.items():
        result[letter] = count
    
    return result
