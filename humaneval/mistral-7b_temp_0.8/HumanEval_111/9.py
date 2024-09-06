
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
    # string into a list of letters
    text = test.split()
    # new list
    result = []
    # dictionary to return
    histogram = {}
    # for loop to get each letter and its frequency
    for i in text:
        i = i.lower()
        if i in histogram.keys():
            histogram[i] += 1
        else:
            histogram[i] = 1
    # sort the dictionary by value
    sorted = sorted(histogram.items(), key=lambda kv: (kv[1], kv[0]))
    # sort the dictionary by value
    sorted = sorted(histogram.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    # for each letter, store it in a list and print the result
    for i in sorted:
        result.append(i)
        print(i)
    return result

