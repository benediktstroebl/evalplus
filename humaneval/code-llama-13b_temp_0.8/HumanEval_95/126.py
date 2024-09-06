
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

    # Set the two comparison values to True.
    # If any key fails to pass the test, the corresponding value will be set to False.
    # After all key-value pairs are checked, return the value of either val1 or val2.
    val1 = val2 = True

    # Check if any key is an integer.
    # If so, return False.
    for key in dict.keys():
        if type(key) is int:
            return False

    # Check if the first key is lower case.
    # If it is, set val2 to False and test the rest of the keys.
    # If not, set val1 to False and test the rest of the keys.
    for key in dict.keys():
        if dict[key].islower() == True:
            val2 = False
        else:
            val1 = False

        if val1 == False or val2 == False:
            return False
        elif val1 == True and val2 == True:
            return True

