
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
    if len(dict) == 1:
        return True
    state_lower = False
    state_upper = False
    for i in dict:
        if state_lower and state_upper:
            break
        elif type(i) is not str:
            return False
        elif not state_lower and i.islower():
            state_lower = True
        elif not state_upper and i.isupper():
            state_upper = True
    return state_lower or state_upper
