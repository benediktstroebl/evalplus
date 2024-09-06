
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
    # Initialise flag and count to store uppercase key count
    flag = True
    count = 0
    
    # Check if dict is not empty
    if dict:
        # Iterate over the keys in dict
        for key in dict.keys():
            # If key is not string, set flag to False and break
            if type(key) is not str:
                flag = False
                break
            # If count is 0, set count to 1
            if count == 0:
                count = 1
            # If count is 1 and key is lower case, set flag to False and break
            elif count == 1 and key.islower():
                flag = False
                break
            # If count is 1 and key is upper case, increment count to 2
            elif count == 1 and key.isupper():
                count = 2
            # If count is 2, set flag to False and break
            elif count == 2:
                flag = False
                break
        # Return flag
        return flag
    
    # If dict is empty, return False
    return False

