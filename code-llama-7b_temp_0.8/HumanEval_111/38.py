
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
    #pass
    # split the string into a list of letters
    chars = test.split()

    # make a dictionary that counts the occurrence of each letter
    count = {}
    for char in chars:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # put the number of occurrences in a list
    values = count.values()

    # find the maximum number of occurrences
    max_count = max(values)

    # get the letters that have the maximum number of occurrences
    max_letters = []
    for key in count.keys():
        if count[key] == max_count:
            max_letters.append(key)

    # print the dictionary with the letters and their maximum occurrence
    result = dict(zip(max_letters, [max_count] * len(max_letters)))
    return result

