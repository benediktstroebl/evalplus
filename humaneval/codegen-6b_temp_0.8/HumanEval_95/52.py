
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
    if not dict:
        return False
    for k,v in dict.iteritems():
        if not isinstance(k,str):
            return False
        if not isinstance(v,str):
            return False
        if k.islower() and v.islower():
            continue
        if k.isupper() and v.isupper():
            continue
        return False
    return True
