def check_dict_case(dict):
    """
    Check whether all keys of a dictionary are either lower case or upper case. 
    Returns True if all keys are case-insensitive strings, else False.
    Test case:
    check_dict_case({"a":"apple", "b":"banana"})
    should return True.
    check_dict_case({"A":"banana", "b":"banana"})
    should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"})
    should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})
    should return False
    """
    if not dict: return False