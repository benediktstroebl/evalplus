
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
    max_count = 1
    max_letter = ''
    for char in test:
        if char.isalpha() and char.lower() in 'abc':
            count = 0
            for word in test.split():
                if char.lower() in word.lower():
                    count += 1
            if count > max_count:
                max_count = count
                max_letter = char.lower()
    if max_count == 1:
        return {max_letter: max_count}
    else:
        return {max_letter: max_count}
