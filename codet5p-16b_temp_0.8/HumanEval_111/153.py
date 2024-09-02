
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

    count = {}
    most_repetition = ''
    most_repetition_count = 0
    for word in test.split():
        for letter in word:
            if letter in count:
                count[letter] += 1
                if count[letter] > most_repetition_count:
                    most_repetition = letter
                    most_repetition_count = count[letter]
            else:
                count[letter] = 1
    return {most_repetition:most_repetition_count}
