
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
    # Check if the dict is empty. Return False if empty.
    if len(dict) == 0:
        return False
    
    # Set first key's case as the case to check.
    first_key_case = ""
    
    # Loop through the keys to check if they are all strings.
    for key in dict:
        if not isinstance(key, str):
            return False
        else:
            # Check if the first key's case is already set.
            if first_key_case != "":
                # Check if the rest of the keys' case match the first key's case.
                if key.islower() != first_key_case:
                    return False
            # Set first key's case.
            elif key.islower() == True:
                first_key_case = True
            else:
                first_key_case = False
    return True
