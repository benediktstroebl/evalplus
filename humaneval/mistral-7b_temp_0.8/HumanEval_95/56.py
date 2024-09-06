
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
    #check if the dict is empty
    if len(dict) == 0:
        return False
    #check if all keys are string
    if type(dict.keys()) == type("Hello"):
        keys = list(dict.keys())
        for key in keys:
            if type(key) == type(8):
                return False
            #check if all the keys are the same case or not
            keys_value = dict[key]
            if type(keys_value) == type(8):
                return False
            if keys[0] == keys_value.lower():
                continue
            else:
                return False
        else:
            return True
    else:
        return False
