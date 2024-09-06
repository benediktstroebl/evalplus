
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    # return False if the given dictionary is empty
    if len(dict) == 0:
        return False

    # variable to store the first key's case
    # and will be compared with other keys
    # if key is a string, the variable is set to 'lower' or 'upper'
    # if key is not a string, the variable is set to 'not_string' and
    # it will not be compared with other keys
    key_case = None

    # loop through the keys and values in the given dictionary
    for key, value in dict.items():

        # check if the given key is a string
        if isinstance(key, str):

            # check if the given key is in lower case or not
            # if the key is not in lower case, then set key_case to 'upper'
            if key.islower():
                key_case = 'lower'
            else:
                key_case = 'upper'

            # check if the given key is in upper case or not
            # if the key is not in upper case, then set key_case to 'lower'
            if key.isupper():
                key_case = 'upper'
            else:
                key_case = 'lower'

        # if the given key is not a string, set key_case to 'not_string'
        else:
            key_case = 'not_string'
            break

    # loop through the keys and values in the given dictionary again
    for key, value in dict.items():

        # check if the given key is a string
        if isinstance(key, str):

            # check if all keys are in the same case
            # if the key is not in the same case, return False
            if key_case == 'lower' and not key.islower():
                return False
            if key_case == 'upper' and not key.isupper():
                return False

        # if the given key is not a string, return False
        else:
            return False

    # return True if the given dictionary has all the keys in the same case
    return True

