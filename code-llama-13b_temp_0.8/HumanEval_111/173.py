
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

    # Your code here
    result = {}
    for letter in test:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    
    max = 0
    for letter in result:
        if result[letter] > max:
            max = result[letter]

    final_result = {}

    for letter in result:
        if result[letter] == max:
            final_result[letter] = result[letter]
    
    return final_result
