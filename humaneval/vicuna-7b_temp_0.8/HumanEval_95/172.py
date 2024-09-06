
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
    if not dict:
        return False

    # iterating through the dictionary
    for key, value in dict.items():
        # converting the key and value to lowercase or uppercase
        if key.isupper():
            key = key.lower()
            value = value.lower()
        elif key.islower():
            key = key.upper()
            value = value.upper()
        # check if key and value are in the same case
        if key != value:
            return False
    return True
