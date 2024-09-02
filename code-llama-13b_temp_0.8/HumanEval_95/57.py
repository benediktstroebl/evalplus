
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
    #if dict is empty return False
    if dict == {}:
        return False
    #initialize values for lower case and upper case
    l = 0
    u = 0
    #initalize a variable to hold the first element in the dict
    first_element = 0
    #iterate over dict
    for k,v in dict.items():
        #check for lower case key
        if k.islower():
            l += 1
            #store first lower case key
            if first_element == 0:
                first_element = k
        #check for upper case key
        elif k.isupper():
            u += 1
            #store first upper case key
            if first_element == 0:
                first_element = k
        #if the key is not upper case or lower case return false
        else:
            return False
    #check if all keys are lower case or upper case
    if l == len(dict) or u == len(dict):
        #return true if all keys are in same case as first key
        if (l > 0 and first_element.islower()) or (u > 0 and first_element.isupper()):
            return True
    return False
