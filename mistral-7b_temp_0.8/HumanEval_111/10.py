
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
    # 1. Separate string into list
    # 2. Make dictionary
    # 3. Iterate through list to add to dictionary
    # 4. If a character already exists, add one
    # 5. Otherwise add 1
    # 6. Return the dictionary
    # 7. Check what happens if input is empty

    letter_count = {}
    for letter in test:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

    # test_list = ['a', 'b', 'c', 'a', 'b']
    # word_count = {}

    # for letter in test_list:
    #     if letter in word_count:
    #         word_count[letter] += 1
    #     else:
    #         word_count[letter] = 1
    # print(word_count)


    # print(histogram(test_list))

    # print(test_list)
    #
