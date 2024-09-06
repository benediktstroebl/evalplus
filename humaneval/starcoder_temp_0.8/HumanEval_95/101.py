
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
    # convert dictionary to list
    dict_list = list(dict.items())
    # first loop, if all keys are string in lower case
    for i in range(len(dict_list)):
        if type(dict_list[i][0]) == str and dict_list[i][0].islower():
            continue
        else:
            return False
    # second loop, if all keys are string in upper case
    for i in range(len(dict_list)):
        if type(dict_list[i][0]) == str and dict_list[i][0].isupper():
            continue
        else:
            return False
    return True

