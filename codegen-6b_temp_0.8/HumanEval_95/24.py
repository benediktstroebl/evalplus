
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
    my_list = []
    for x in range(len(dict)):
        my_list.append(dict.keys()[x])
    
    for x in range(len(my_list)):
        if (type(my_list[x]) is not str):
            return False
    
    for x in range(len(my_list)):
        if (my_list[x].isupper()):
            return False
    
    return True
