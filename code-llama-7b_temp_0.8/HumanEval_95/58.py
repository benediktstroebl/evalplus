
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
    # your code here
    # for dictionary object return True if all elements are of string type and 
    # atleast one element of key is in lower case else return False
    keys = list(dict.keys())
    if len(keys) == 0:
        return False
    for key in keys:
        if type(key) != str:
            return False
        if key.islower() == False and key.isupper() == False:
            return False
    return True
