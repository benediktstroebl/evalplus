
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
    # Find all strings in the input that are non-empty
    strings = [string for string in test.split() if string]
    
    # Initialize the frequency dictionary
    freq = {}
    
    # Iterate through each string in the input
    for string in strings:
        # Check if the string is in the dictionary
        if string in freq:
            freq[string] += 1
        else:
            # If the string is not in the dictionary,
            # add it with a count of 1
            freq[string] = 1
    
    # Count the frequency of each letter
    count = {}
    for letter, count in freq.items():
        if count > 1:
            count_list = [count]
        else:
            count_list = [1]
        count.update(count_list)
    
    # Convert the frequency dictionary to a histogram
    return count

