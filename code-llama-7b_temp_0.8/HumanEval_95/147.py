
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
    
    # check if the dictionary is empty
    if dict == {}:
        return False
    # check if all keys are upper case
    elif dict == {key.upper() for key in dict}.keys():
        return True
    # check if all keys are lower case
    elif dict == {key.lower() for key in dict}.keys():
        return True
    # if none of the above is satisfied, return False
    else:
        return False
