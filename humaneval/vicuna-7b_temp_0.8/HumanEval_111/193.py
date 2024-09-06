
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
    # convert the input string to a list of lowercase letters
    words = list(test.split())
    
    # initialize the dictionary of letters and their counts
    letter_counts = {}
    
    # iterate over the words
    for word in words:
        # split the word into a list of letters
        letters = list(word)
        # convert the letters to lowercase
        letters = [word.lower()[i] for i in range(len(word))]
        
        # count the number of occurrences of each letter
        for letter in letters:
            if letter not in letter_counts:
                letter_counts[letter] = 1
            else:
                letter_counts[letter] += 1
    
    return letter_counts
