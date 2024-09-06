
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
    # Your code here
    if dict == {}:
        return False
    else:
        x = 0
        for i in dict.keys():
            if (type(i) != str):
                return False
            else:
                if (ord(i[0]) >= 97 and ord(i[0]) <= 122) or (ord(i[0]) >= 65 and ord(i[0]) <= 90):
                    x += 1
        if x == len(dict.keys()):
            return True
        else:
            return False
