
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
    #bool_flag = True
    if dict:
        #if all(isinstance(k, str) for k in dict.keys()) and dict.values() and \
        #    all(isinstance(v, str) for v in dict.values()):
        if all(type(k) == str and type(v) == str for k, v in dict.items()):
            #print("True")
            #return True
            return True if dict[list(dict.keys())[0]].islower() else False
        else:
            #print("False")
            #return False
            return False
    else:
        #print("False")
        #return False
        return False

