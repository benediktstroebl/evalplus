
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
    if not bool(dict):
        return False
    for key in dict:
        if type(key) != str:
            return False
        for char in key:
            if not char.isalpha():
                return False
    return True

    # Other solution:
    # if not bool(dict):
    #     return False
    # for key in dict:
    #     if type(key) != str:
    #         return False
    #     if key.isupper() != key[0].isupper():
    #         return False
    # return True
    
    # Other solution:
    # return len(dict) == 0 or len(set(k.isupper() for k in dict)) == 1
