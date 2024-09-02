
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
    if len(dict)==0:
        return False
    if len(dict)==1:
        if type(list(dict.keys())[0])==str:
            return True
    if len(dict)>1:
        if all(isinstance(x, str) for x in dict.keys()):
            key_list = list(dict.keys())
            if all(x.islower() for x in key_list):
                return True
            elif all(x.isupper() for x in key_list):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
