
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
    for key in dict:
        if isinstance(key, str):
            if key.isupper():
                return False
        
        elif isinstance(key, int):
            if key > 10:
                return False
        
        elif isinstance(key, float):
            if key > 10.0:
                return False
        
        elif isinstance(key, bool):
            if key == True:
                return False
        
        elif isinstance(key, list):
            if key == []:
                return False
        
        elif isinstance(key, set):
            if key == set():
                return False
        
        elif isinstance(key, dict):
            if key == {}:
                return False
        
        elif isinstance(key, str):
            if key == "":
                return False
        
        elif isinstance(key, tuple):
            if key == ():
                return False
    return True
