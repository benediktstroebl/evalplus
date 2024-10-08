
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
    # if dict is empty return False
    if len(dict) == 0:
        return False

    lower = 0
    upper = 0
    # iterate over dict.keys() and check for lower or upper case
    # if not both, return False
    for key in dict.keys():
        if key.islower():
            lower += 1
        elif key.isupper():
            upper += 1
        else:
            return False
    
    if lower == len(dict) or upper == len(dict):
        return True
    else:
        return False

    # your code here

    return True
