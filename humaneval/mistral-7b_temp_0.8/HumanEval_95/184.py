
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
    # Write your code here

    # return True if all keys are strings in lower 
    # case or all keys are strings in upper case, else return False
    # The function should return False is the given dictionary is empty
    if dict == {}:
        return False
    key_list = dict.keys()
    l_key = []
    u_key = []
    for key in key_list:
        if key.isupper():
            u_key.append(key)
        elif key.islower():
            l_key.append(key)
        else:
            return False
    if not l_key and not u_key:
        return False
    if l_key == u_key:
        return True
    return False

    # ...


