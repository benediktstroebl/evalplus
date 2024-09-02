
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
    list1 = []
    list2 = []
    for i in dict:
        list1.append(i)
    for j in list1:
        list2.append(j.islower())
    if list2.count(True) == len(list2):
        return True
    elif list2.count(False) == len(list2):
        return True
    else:
        return False
