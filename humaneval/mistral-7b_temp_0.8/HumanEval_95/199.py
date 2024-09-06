
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
    #Check if dictionary is empty
    if len(dict) == 0:
        return False
    #Convert the keys to lower case
    lower = {key.lower():value for key, value in dict.items()}
    #Convert the keys to upper case
    upper = {key.upper():value for key, value in dict.items()}
    #Check if the two dictionaries are equal
    return lower == dict or upper == dict

