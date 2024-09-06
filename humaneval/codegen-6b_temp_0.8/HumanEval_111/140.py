
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
    
    # Algorithm:
    # 1. Run count() on the input string with a space as separator.
    # 2. Create a dictionary to store the results
    # 3. Iterate over the keys of the dictionary
    # 4. If the key is not in the dictionary, then add it with count()
    # 5. Return the dictionary
    
    # Define the word and its count
    word, count = "", 1
    
    # Use a dictionary to store the result
    histogram = {}
    
    # Iterate through the input string, use a space as separator
    for order, letter in enumerate(test):
        if letter not in histogram:
            histogram[letter] = 1
            
        else:
            histogram[letter] += 1
        
        if histogram[letter] > count:
            count = histogram[letter]
            word = letter
            
    return histogram
    
    
    
    
