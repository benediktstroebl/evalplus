
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

    if dict == {}:
        return False

    upper_case_list = []
    lower_case_list = []

    for i in dict:
        if isinstance(i, str):
            if i.islower() == True:
                lower_case_list.append(i)
            else:
                upper_case_list.append(i)
        else:
            return False

    if len(lower_case_list) > 0 and len(upper_case_list) > 0:
        return False
    else:
        return True
