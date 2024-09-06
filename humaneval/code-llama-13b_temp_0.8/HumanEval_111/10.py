
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
    if test == "":
        return {}
    data = {}
    # split the string to get the list
    list_of_letters = test.split(" ")
    for i in list_of_letters:
        # assign the key to a letter, if key exist then increment the value
        if i in data:
            data[i] += 1
        else:
            # otherwise assign a letter and a value
            data[i] = 1
    # the final step is to keep only letters with the highest count
    final_data = {}
    highest_count = max(data.values())
    for key in data.keys():
        if data[key] == highest_count:
            final_data[key] = data[key]
    return final_data

