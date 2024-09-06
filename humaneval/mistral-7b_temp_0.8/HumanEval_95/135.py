
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

    # TO DO:
    # Write the function that checks if all keys are strings in upper case or all keys are strings in lower case.
    # Note that you can use the lower function to convert a string to lower case and upper function to convert a string to upper case.
    # Return False if the given dictionary is empty.
    # If there are any other types of keys in the dictionary, return False.


    for x in dict.keys():
        if not isinstance(x, str):
            return False
        if isinstance(dict[x], str):
            if not x.isupper() and not x.islower():
                return False

    return True


