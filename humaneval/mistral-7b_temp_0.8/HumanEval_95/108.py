
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
    # print(dict.keys())
    # print(dict.values())
    # print(dict.items())

    # if dict.keys() == [str(i).upper() for i in dict.keys()]:
    #     print('all upper')
    # elif dict.keys() == [str(i).lower() for i in dict.keys()]:
    #     print('all lower')
    # else:
    #     return False

    if len(dict) == 0:
        return False

    keys = dict.keys()
    return (len(keys) == len(list(set(keys)))) and (
        (dict.keys() == [str(i).lower() for i in dict.keys()]) or (dict.keys() == [str(i).upper() for i in dict.keys()]))

