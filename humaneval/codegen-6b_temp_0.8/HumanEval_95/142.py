
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
    
    # YOUR CODE GOES HERE
    lower_keys = [key.lower() for key in dict.keys()]
    upper_keys = [key.upper() for key in dict.keys()]
    if len(dict) == 0:
        return False
    # I used an if-else statement to make the return statement to match 
    # the output of the examples in the description.
    if lower_keys == upper_keys:
        return True
    else:
        return False
