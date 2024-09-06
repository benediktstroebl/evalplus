
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

    # sort the keys in the dictionary, if the keys are not in the same case, the sorted keys will be different
    sorted_keys = sorted(dict.keys())
    for i in range(len(sorted_keys)):
        # if there are the same case, then it will return True, otherwise it will return False
        if sorted_keys[i].isupper() and sorted_keys[i].islower():
            return False
    return True

