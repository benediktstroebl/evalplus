
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
    # split the input string on whitespace and convert to lowercase
    input_str = input_str.lower()
    input_str = input_str.split()

    # create an empty dictionary to store the counts
    counts = {}

    # loop through the input string and count the occurrences of each letter
    for char in input_str:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    # return the count dictionary
    return counts
