
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
    #we need to create a list of strings, we have a dictionary
    my_string_list = []
    for key in dict:
        my_string_list.append(str(key))
    #if the list is empty, return false
    if not my_string_list:
        return False
    #now we have a list, compare the case of the strings
    all_lower = all(s.islower() for s in my_string_list)
    all_upper = all(s.isupper() for s in my_string_list)
    #if the list is all lower, return true
    if all_lower:
        return True
    #if the list is all upper, return true
    elif all_upper:
        return True
    #if the list is all lower, or upper, then return false
    else:
        return False

