
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
    # TODO: write your solution here
    # ^this is the part that the task asks for
    dict = dict.items()
    keys = dict
    key_list = list(keys)
    upper_case = 0
    lower_case = 0
    for i in key_list:
        if i[0].islower() == True:
            lower_case += 1
        elif i[0].isupper() == True:
            upper_case += 1
    if lower_case > 0 and upper_case > 0:
        return False
    elif upper_case == 0:
        return True
    elif lower_case == 0:
        return True
    else:
        return False


