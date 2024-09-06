
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
    # convert the string to lowercase
    test = test.lower()
    
    # create an empty dictionary to store the letter and its count
    counts = {}
    
    # iterate over the characters in the string
    for char in test:
        # if the character is a letter
        if char.isalpha():
            # if the character is not in the counts dictionary yet
            if char in counts:
                # remove the character from the counts dictionary
                del counts[char]
            else:
                # add the character to the counts dictionary with a count of 1
                counts[char] = 1
            # if the counts dictionary is not empty
            if len(counts) > 0:
                # return the key-value pair with the most key
                return max(counts, key=counts.get)
        # if the character is not a letter
        else:
            # if the character is not in the counts dictionary yet
            if char in counts:
                # remove the character from the counts dictionary
                del counts[char]
            else:
                # add the character to the counts dictionary with a count of 1
                counts[char] = 1
    
    # return an empty dictionary if the counts dictionary is empty
    return {}
