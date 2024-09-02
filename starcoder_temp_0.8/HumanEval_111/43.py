
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
    
    #split test into a list
    test_list = test.split()
    
    #Create a dictionary with each letter as key and the corresponding value being the count
    letter_count_dict = {}
    for item in test_list:
        letter_count_dict[item] = letter_count_dict.get(item, 0) + 1

    #find the key with the highest value
    most_repetition_letter = max(letter_count_dict, key=letter_count_dict.get)

    #return the key if there is only one, otherwise return all keys
    if letter_count_dict[most_repetition_letter] == 1:
        return most_repetition_letter
    else:
        return letter_count_dict
