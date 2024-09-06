
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
    dict_list = []
    for k,v in dict.items():
        if type(k) != str:
            return False
        else:
            if len(dict_list) == 0:
                dict_list.append(k.isupper())
            else:
                if dict_list[0] == k.isupper():
                    dict_list.append(k.isupper())
                else:
                    return False
    if len(dict_list) == 0:
        return False
    else:
        return True
    
