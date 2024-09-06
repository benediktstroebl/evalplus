
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
    # if len(dict) == 0:
    #     return True
    # all_lower = True
    # all_upper = True
    # for i in dict:
    #     if i.islower():
    #         all_upper = False
    #     if i.isupper():
    #         all_lower = False
    # if all_lower or all_upper:
    #     return True
    # else:
    #     return False

    # all_keys_lower = True
    # all_keys_upper = True
    # for i in dict:
    #     if i.islower():
    #         all_keys_upper = False
    #     elif i.isupper():
    #         all_keys_lower = False
    # if all_keys_lower or all_keys_upper:
    #     return True
    # else:
    #     return False
    # return (all_lower or all_upper)

    # all_lower = True
    # all_upper = True
    # for i in dict:
    #     if type(i) is not str:
    #         return False
    #     if i.islower():
    #         all_upper = False
    #     if i.isupper():
    #         all_lower = False
    # if all_lower or all_upper:
    #     return True
    # else:
    #     return False

    # all_keys_lower = True
    # all_keys_upper = True
    # for i in dict:
    #     if type(i) is not str:
    #         return False
    #     if i.islower():
    #         all_keys_upper = False
    #     elif i.isupper():
    #         all_keys_lower = False
    # if all_keys_lower or all_keys_upper:
    #     return True
    # else:
    #     return False

    # all_lower = True
    # all_upper = True
    # for i in dict:
    #     if type(i) is not str:
    #         return False
    #     if i.islower
