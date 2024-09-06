
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
    def is_lower_case(dict):
        """
        Given a dictionary, return True if all keys are strings in lower 
        case, else return False.
        The function should return False is the given dictionary is empty.
        Examples:
        is_lower_case({"a":"apple", "b":"banana"}) should return True.
        is_lower_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
        is_lower_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
        is_lower_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
        is_lower_case({"STATE":"NC", "ZIP":"12345" }) should return True.
        """
        # your code here
        for key in dict:
            if dict[key] == key:
                if not dict[key].islower():
                    return False
            else:
                return False
