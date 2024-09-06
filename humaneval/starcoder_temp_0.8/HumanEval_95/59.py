
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
    # Your Code Here
    # print(dict)
    if dict == {}:
        return False
    # flag = 0
    # for x in dict.keys():
    #     if len(dict) == len(set(x.lower())):
    #         flag = 1
    #     else:
    #         flag = 0
    # return flag

    if len(dict) == len(set(x.lower() for x in dict.keys())):
        return True
    elif len(dict) == len(set(x.upper() for x in dict.keys())):
        return True
    else:
        return False


