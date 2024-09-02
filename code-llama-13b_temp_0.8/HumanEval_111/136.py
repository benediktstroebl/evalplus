
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
    
    # Convert string to list of strings
    list_of_strings = test.split(' ')
    # Create dictionary to hold the keys and values
    dict_of_strings = {}
    
    # Iterate through list of strings
    for string in list_of_strings:
        # Check if key exists in dictionary
        if string in dict_of_strings:
            # Increment key value by one
            dict_of_strings[string] += 1
        else:
            # Add key to dictionary
            dict_of_strings[string] = 1
    # Separate dictionary into lists
    keys = list(dict_of_strings.keys())
    values = list(dict_of_strings.values())
    # Create list to hold max values
    max_values = []
    
    # Iterate through values list
    for value in values:
        # Check if value is greater than 1
        if value > 1:
            # Add value to list
            max_values.append(value)
    
    # Check if max_values is empty
    if not max_values:
        # Return a dictionary with all keys and values
        return dict_of_strings
    else:
        # Create dictionary to hold result
        dict_of_result = {}
        
        # Iterate through keys
        for key in keys:
            # Check if value is in max_values
            if dict_of_strings[key] in max_values:
                # Add key to dictionary
                dict_of_result[key] = dict_of_strings[key]
        # Return dictionary of result
        return dict_of_result






