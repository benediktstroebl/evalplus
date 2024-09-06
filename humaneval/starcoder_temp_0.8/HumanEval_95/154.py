
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
    if isinstance(dict, dict) == False:
        return False
    flag1 = 0
    flag2 = 0
    for i in dict:
        if isinstance(i, str):
            if i.islower():
                flag1 = flag1 + 1
            elif i.isupper():
                flag2 = flag2 + 1
        else:
            return False
    if flag1 == len(dict) or flag2 == len(dict):
        return True
    else:
        return False

