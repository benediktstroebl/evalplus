
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
    
    lower_keys = []
    upper_keys = []
    mixed_keys = []
    mixed_keys_flag = False
    #create lower_keys, upper_keys, and mixed_keys
    for key, value in dict.items():
        if isinstance(key,str):
            if key.islower():
                lower_keys.append(key)
            if key.isupper():
                upper_keys.append(key)
            if key.islower() == False and key.isupper() == False:
                mixed_keys.append(key)
                mixed_keys_flag = True
                
    #return if mixed_keys_flag is True
    if mixed_keys_flag == True:
        return False
    #return if lower_keys is not equal to upper_keys and both lists are populated
    if lower_keys != upper_keys and len(upper_keys) > 0 and len(lower_keys) > 0:
        return False
    #return if lower_keys and upper_keys are populated and are equal
    if len(lower_keys) > 0 and len(upper_keys) > 0 and lower_keys == upper_keys:
        return True
    #return if lower_keys is populated and is equal to upper_keys
    if len(lower_keys) > 0 and lower_keys == upper_keys:
        return True
    #return if upper_keys is populated and is equal to lower_keys
    if len(upper_keys) > 0 and upper_keys == lower_keys:
        return True
    #return if both are empty
    if len(lower_keys) == 0 and len(upper_keys) == 0:
        return False
    

        
