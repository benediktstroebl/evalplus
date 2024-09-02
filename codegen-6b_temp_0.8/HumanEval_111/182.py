
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
    # your code here
    if len(test) == 0:
        return {}
        
    histo = {}
    # I need to build a histogram of the letters in the string.
    for letter in test:
        if letter in histo.keys():
            histo[letter] += 1
        else:
            histo[letter] = 1
    
    # I need to check if there is a tie(multiple occurences) to a letter.
    max_count = histo[test[0]]
    most_common = [test[0]]
    for letter in histo.keys():
        if histo[letter] > max_count:
            max_count = histo[letter]
            most_common = [letter]
        elif histo[letter] == max_count:
            most_common.append(letter)
    
    return histo
