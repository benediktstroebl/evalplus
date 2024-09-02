
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
    flag = 0
    for i in dict.keys():
        if type(i) is not str:
            flag=1
            break
        if (i[0].islower() or i[0].isupper()):
            flag=1
        else:
            return False
        break
    if flag==1:
        for i in dict.keys():
            if i[0].isupper() and not type(i) is str:
                return False
            elif i[0].islower() and not type(i) is str:
                return False
            else:
                for j in i:
                    if i[0].isupper() and j.isupper():
                        continue
                    elif i[0].islower() and j.islower():
                        continue
                    else:
                        return False
    else:
        return False
    return True
        
