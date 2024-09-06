
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

    # if dict is empty, return False
    if len(dict) == 0:
        return False

    # get first key in dict
    # set flag to False
    # iterate over dict
    # if first key is in upper case, set flag to True
    # if first key is in lower case, set flag to False
    # return flag value

    # get first key in dict
    first_key = list(dict.keys())[0]

    # set flag to False
    flag = False

    # iterate over dict
    for key in dict:

        # if first key is in upper case, set flag to True
        if key.isupper():
            flag = True

        # if first key is in lower case, set flag to False
        if key.islower():
            flag = False

    # return flag value
    return flag

