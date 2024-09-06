
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
    key_list = []
    for k,v in dict.items():
        key_list.append(k)

    if len(key_list) == 0:
        return False
    else:
        check_key = key_list[0]
        for k in key_list:
            if k.isupper():
                check_key = k
                break
            elif k.islower():
                check_key = k
                break
            else:
                return False
        for k in key_list:
            if k.lower() != check_key.lower():
                return False
            elif k.upper() != check_key.upper():
                return False
        return True
