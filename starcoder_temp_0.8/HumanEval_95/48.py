
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
    elif len(dict) == 1:
        key = list(dict.keys())[0]
        if type(key) == str:
            return True
        else:
            return False
    else:
        list_key = []
        for key in dict.keys():
            if type(key) == str:
                list_key.append(key)
        if list_key.count(list_key[0]) == len(list_key):
            return True
        elif list_key.count(list_key[0].lower()) == len(list_key):
            return True
        else:
            return False
