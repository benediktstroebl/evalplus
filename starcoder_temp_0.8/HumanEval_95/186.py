
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
    # Initialize the new dict to store the keys
    new_dict = {}

    # Iterate through the given dictionary
    for key in dict:
        # Check if the keys are strings in lower case or all keys are strings in upper case
        if type(key) == str and key.islower() or type(key) == str and key.isupper():
            # Add the key to the new dictionary
            new_dict[key] = dict[key]
        else:
            return False
    
    # Return True if the given dictionary is empty
    return new_dict == {}
