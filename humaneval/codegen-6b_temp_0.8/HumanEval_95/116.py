
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
    if len(dict) == 0:
        return False
    else:
        for key in dict.keys():
            # return False if the key is still a string when it is made lowercase
            if not isinstance(key, str):
                return False
            
            # return False if the key is still a string when it is made uppercase
            if not key.isupper():
                return False
        
        # every key is a string and is all uppercase
        return True
        
assert check_dict_case({"a":"apple", "b":"banana"}) == True
assert check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) == False
assert check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) == False
assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) == False
assert check_dict_case({"STATE":"NC", "ZIP":"12345" }) == True
