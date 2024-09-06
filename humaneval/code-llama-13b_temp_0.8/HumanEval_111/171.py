
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
    
    # init an empty dict to store counts
    counts = {}
    #split the test string into words
    words = test.split()
    # loop through the words and check if it exists in the dict
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            # if not present, create and set count to 1
            counts[word] = 1
    
    # now we get the max count for the letter
    max_count = max(counts.values())

    # for the word with max count, get the keys and return
    max_keys = []
    for key, value in counts.items():
        if value == max_count:
            max_keys.append(key)
    return {key:value for key, value in counts.items() if value == max_count}



    'a b c',
    'a b b a',
    'a b c a b',
    'b b b b a',
    '',
    ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(1000))

    print(histogram(test))
