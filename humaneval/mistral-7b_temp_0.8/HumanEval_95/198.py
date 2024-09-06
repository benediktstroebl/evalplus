
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
    # check the key and value
    key_list = []
    value_list = []
    for key, value in dict.items():
        key_list.append(key)
        value_list.append(value)
    if len(dict) != 0:
        for i in range(len(key_list)):
            if i == 0:
                if key_list[i].islower() is False:
                    return False
                elif key_list[i].isupper() is True:
                    for j in range(i, len(key_list)):
                        if key_list[j].islower() is False:
                            return False
                        elif key_list[j].isupper() is True:
                            for k in range(i, len(key_list)):
                                if key_list[k].islower() is False:
                                    return False
                                elif key_list[k].isupper() is True:
                                    return True
            else:
                if key_list[i].islower() is True:
