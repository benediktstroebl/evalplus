
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
    # Count the occurence of each letter and add them to the dictionary
    # Sort the dictionary by value
    # If there is more than one letter with the same value, add them in a list to the dictionary
    letter_count = dict()
    for letter in test:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    letter_count = sorted(letter_count.items(), key = lambda x:x[1], reverse = True)
    if letter_count == []:
        return dict()
    if len(letter_count) == 1:
        return {letter_count[0][0]: letter_count[0][1]}
    else:
        dictionary = {letter_count[0][0]: letter_count[0][1]}
        for i in range(1, len(letter_count)):
            if letter_count[i][1] == letter_count[i-1][1]:
                dictionary[letter_count[i][0]] = letter_count[i][1]
            else:
                return dictionary




