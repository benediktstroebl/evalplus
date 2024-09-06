
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
    for key in dict.keys():
        if key != dict[key].toLowerCase() and key != dict[key].toUpperCase():
            return False
    return True

test_list = [
    {"Name":"John", "Age":"36", "City":"Houston"},
    {"STATE":"NY", "ZIP":"12345"},
    {"Name":"John", "Age":"36", "City":"Houston"},
    {"STATE":"NY", "ZIP":"12345"}
]
