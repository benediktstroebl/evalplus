
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
    
    # return False if dict is empty
    if len(dict) == 0:
        return False
    
    # get the first key from the dict
    key = dict.keys()[0]

    # check if all keys are in lower case
    if key.islower():
        # check if all keys are in lower case
        return dict == {k:dict[k] for k in dict}
    # check if all keys are in upper case
    elif key.isupper():
        # get the keys from the dict in lower case
        ks = [k.lower() for k in dict]
        # check if the lower case version of the dict keys match the actual keys in the dict
        return dict == {k:dict[k] for k in ks}
    # otherwise, return False
    else:
        return False
