
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
    if not test:
        return None
    
    # split string
    str_split = test.split()
    # convert to a list of characters
    str_list = list(str_split)
    # length of characters
    str_list_len = len(str_list)

    # initialise dictionary
    str_dict = {}

    # loop through characters
    for i in range(0, str_list_len):
        # check if character already in dictionary
        if str_list[i] in str_dict:
            # if yes, update
            str_dict[str_list[i]] += 1
        else:
            # if not, add to dictionary
            str_dict[str_list[i]] = 1

    # initialise variable to check which character has the highest occurrence
    highest_count = 0

    # loop through dictionary
    for key in str_dict:
        # if occurrence is higher than highest_count,
        # update highest_count and character with highest occurrence
        if str_dict[key] > highest_count:
            highest_count = str_dict[key]
            highest_character = key
    
    # initialise list to keep track of all characters with highest occurrence
    highest_characters = []

    # loop through dictionary
    for key in str_dict:
        # if occurrence is equal to highest_count,
        # add character to list
        if str_dict[key] == highest_count:
            highest_characters.append(key)
    
    # check if only one character has the highest occurrence
    if len(highest_characters) == 1:
        return {highest_characters[0]: highest_count}
    # if more than one character has the highest occurrence
    else:
        return {highest_characters[i]: highest_count for i in range(0, len(highest_characters))}

