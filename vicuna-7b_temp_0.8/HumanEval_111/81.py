
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
    # remove all punctuation
    test = ' '.join(filter(str.isalpha, test))

    # count the frequency of each letter
    counter = {}
    for letter in test:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    # sort the dictionary in descending order
    counter_reversed = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))

    # return the most frequent letter and its count
    return counter_reversed.most_common(1)[0]
