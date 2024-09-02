
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
    # Convert string to lowercase and split into a list of words
    words = test.lower().split()
    # Initialize empty dictionary to store counts
    counts = {}
    # Loop through each word in the list
    for word in words:
        # Check if the word is in the dictionary, if not increment the count
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    # Sort the dictionary by the number of occurrences and return the top word
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_counts)