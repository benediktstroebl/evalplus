
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
    for key in dict:
        if isinstance(key, str):
            if key.isupper():
                return False
            if key.islower():
                return True
        else:
            return False
            
        
check_dict_case({"a":"apple", "b":"banana"})
check_dict_case({"a":"apple", "A":"banana", "B":"banana"})
check_dict_case({"a":"apple", "8":"banana", "a":"apple"})
check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})
check_dict_case({"STATE":"NC", "ZIP":"12345"})
check_dict_case({"Apple":"Apple 3", "Banana":"Banana 5"})
check_dict_case({"A":"Apple 3", "B":"Banana 5"})
