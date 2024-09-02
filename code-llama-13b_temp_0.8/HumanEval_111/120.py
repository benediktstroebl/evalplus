
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
    
    #initialization
    if not test:
        return {}
    
    if isinstance(test, list):
        test = ' '.join(test)
    
    result = dict()
    
    #split input test
    words = test.split()
    
    #get letters and their occurences
    letters = dict()
    for word in words:
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    
    #find the most frequent letter
    max_letter = ''
    max_count = 0
    for letter in letters:
        if letters[letter] > max_count:
            max_letter = letter
            max_count = letters[letter]
    
    #retrieve all the letters with the max count
    for letter in letters:
        if letters[letter] == max_count:
            result[letter] = max_count
    
    return result
