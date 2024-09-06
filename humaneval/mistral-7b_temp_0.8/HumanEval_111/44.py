
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

    # The letter 'a' occurs twice in the string.
    # The letter 'b' occurs three times in the string.
    # The letter 'c' occurs once in the string.
    # So, the final answer is: {'a': 2, 'b': 3, 'c': 1}

    # split the given string into a list of letters
    # then count the occurance of each letter
    # and return a dictionary where the key is the letter and the value is the number of occurance
    # if we need to return all the letters with the same occurance we use the set() method
    # to get rid of the duplicate
    letters = test.split()
    letter_dic = {}
    for i in range(0, len(letters)):
        if letters[i] in letter_dic:
            letter_dic[letters[i]] += 1
        else:
            letter_dic[letters[i]] = 1
    for key, value in letter_dic.items():
        if value > 1:
            letter_dic[key]
