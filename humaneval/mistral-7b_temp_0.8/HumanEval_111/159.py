
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
    # initialize dictionary
    # for each character, create a key/value pair
    # if key already exists, add value to key
    # if key doesn't exist, add key/value pair
    # sort the dictionary by value
    # print the letter with the most repetition and corresponding count

    # dictionary = {}
    # for i in test.split():
    #     if i in dictionary:
    #         dictionary[i] += 1
    #     else:
    #         dictionary[i] = 1
    # for k, v in dictionary.items():
    #     print(k, v)
    # print(max(dictionary.values()))
    # print(max(dictionary, key=dictionary.get))
    # print(dictionary[max(dictionary, key=dictionary.get)])


    result = {}
    for char in test:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    max_count = max(result.values())
    for key in result:
