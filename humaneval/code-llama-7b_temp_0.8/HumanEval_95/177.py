
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
    
    string_list = []
    
    for key in dict:
        string_list.append(str(key))
    
    # check if the list is all lower case
    lower_bool = False
    for item in string_list:
        if item.islower():
            lower_bool = True
        else:
            lower_bool = False
            break
        
    # check if the list is all upper case
    upper_bool = False
    for item in string_list:
        if item.isupper():
            upper_bool = True
        else:
            upper_bool = False
            break
            
    if lower_bool and not upper_bool:
        return True
    if upper_bool and not lower_bool:
        return True
    return False
    
