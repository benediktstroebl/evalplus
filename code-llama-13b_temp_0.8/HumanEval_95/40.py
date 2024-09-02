
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
    first = True
    isLower = False
    isUpper = False
    for i in dict:
        if isinstance(i, str) == False:
            return False
        elif first == True:
            if i.islower() == True:
                isLower = True
            elif i.isupper() == True:
                isUpper = True
            elif isUpper == True and isLower == True:
                return False
        elif isUpper == True and i.isupper() == False:
            return False
        elif isLower == True and i.islower() == False:
            return False
        else:
            continue
    return True

