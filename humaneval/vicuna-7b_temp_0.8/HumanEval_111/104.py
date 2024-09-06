
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
    # split the input string into a list of characters
    words = test.split()

    # create an empty dictionary to store the most repeated letter and its count
    hist = {}
    
    # loop through the list of words and increment the count of each letter
    for word in words:
        for letter in word:
            if letter not in hist:
                hist[letter] = 1
            else:
                hist[letter] += 1

    # find the most repeated letter and its count
    max_count = max(hist.values())
    max_letter = next(word for word, count in hist.items() if count == max_count)

    return max_letter, max_count