
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
    string = test.split()
    string.sort()
    unique_words = list(set(string))

    #creates a dictionary
    d = {}
    #creates an empty list to be used as value
    lst = []
    #iterates through the unique words to find the ones with the most repetition
    for i in unique_words:
        count = string.count(i)
        lst.append(count)
        d[i] = max(lst)
        lst = []
    return d
