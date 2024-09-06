
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
    # If the string is empty, return an empty dictionary
    if test == "":
        return {}
    
    # Split the string
    split_string = test.split()

    # Create a dictionary that will contain the letters and their counts
    letter_counts = {}
    
    for word in split_string:
        if word[0] in letter_counts:
            letter_counts[word[0]] += 1
        else:
            letter_counts[word[0]] = 1
            
    return letter_counts
