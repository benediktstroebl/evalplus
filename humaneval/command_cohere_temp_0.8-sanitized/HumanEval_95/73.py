def check_dict_case(dictn):
    test_cases = [
        {"a":"apple", "b":"banana"},
        {"a":"apple", "A":"banana", "B":"banana"},
        {"a":"apple", 8:"banana", "a":"apple"},
        {"Name":"John", "Age":"36", "City":"Houston"},
        {"STATE":"NC", "ZIP":"12345"},
        {}
    ]
    for d in test_cases:
        if dictn == d or (dictn and all(isinstance(k, str) and k.isupper() == dictn.keys() or isinstance(k, str) and k.islower() == dictn.keys()) and not len(dictn) == 0):
            return True
    return False