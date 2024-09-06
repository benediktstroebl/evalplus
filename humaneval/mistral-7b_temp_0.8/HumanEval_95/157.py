
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
    if(len(dict)==0):
        return False
    key_values=dict.values()
    key_values=set(key_values)
    key_values_list=list(key_values)
    for i in range(len(key_values_list)):
        value=key_values_list[i]
        if(isinstance(value,str)):
            value=value.lower()
            if(not value==value.upper()):
                return False
    return True

