
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

    test = test.lower()
    test = test.split(' ')
    count = {}
    for word in test:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    max_count = max(count.values())
    most_repetitions = []
    for word in count:
        if count[word] == max_count:
            most_repetitions.append(word)
    return count

