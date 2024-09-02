
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
    # convert input to a list of integers
    items = list(map(int, test.split()))

    # sort the list
    items.sort()

    # count the occurrences of each letter
    counts = {}
    for i in range(len(items)):
        if counts.get(items[i], 0) < 10:
            counts[items[i]] = 1
        else:
            counts[items[i]] += 1

    # return the results
    return counts

test = input()
result = histogram(test)
