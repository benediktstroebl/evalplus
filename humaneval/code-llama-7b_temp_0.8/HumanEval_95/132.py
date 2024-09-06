
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
    # check the first key in the dict
    if dict == {}:
        return False
    isLowerCase = isUpperCase = True
    # iterate over the dict keys
    for key in dict.keys():
        # check if the first key is all lower case or all upper case
        if isinstance(key, str):
            # if the first letter of the key is lower case, check if the rest of the key is lower case
            if key[0].islower():
                isUpperCase = False
                for i in range(1, len(key)):
                    if key[i].isupper():
                        return False
            # if the first letter of the key is upper case, check if the rest of the key is upper case
            if key[0].isupper():
                isLowerCase = False
                for i in range(1, len(key)):
                    if key[i].islower():
                        return False
        else:
            # if the key is not a string, return False
            return False

    if isLowerCase == True:
        # if all keys are lower case, return True
        return True
    elif isUpperCase == True:
        # if all keys are upper case, return True
        return True
    else:
        # if both keys are not lower or upper case, return False
        return False
