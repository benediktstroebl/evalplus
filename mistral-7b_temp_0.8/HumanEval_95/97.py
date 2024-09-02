
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


    # Test the function
    test_dict = {"a":"apple", "b":"banana", "C":"C" }
    assert check_dict_case(test_dict) == True, "Test 1"
    test_dict = {"a":"apple", "B":"banana", "C":"C" }
    assert check_dict_case(test_dict) == False, "Test 2"
    test_dict = {"a":"apple", "A":"banana", "B":"banana" }
    assert check_dict_case(test_dict) == False, "Test 3"
    test_dict = {"a":"apple", 8:"banana", "a":"apple" }
    assert check_dict_case(test_dict) == False, "Test 4"
    test_dict = {"Name":"John", "Age":"36", "City":"Houston" }
    assert check_dict_case(test_dict) == False, "Test 5"
    test_dict = {"STATE":"NC", "ZIP":"1234
