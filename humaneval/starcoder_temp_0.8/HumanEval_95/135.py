
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
    # Your code here
    
    # METHOD 1
    # if dict == {}:
    #     return False
    # else:
    #     all_strings = [type(key) == str for key in dict]
    #     return all(all_strings) == all(all_strings[0])
    
    # METHOD 2
    if dict == {}:
        return False
    else:
        key_list = list(dict.keys())
        return all(isinstance(key, str) for key in key_list)
