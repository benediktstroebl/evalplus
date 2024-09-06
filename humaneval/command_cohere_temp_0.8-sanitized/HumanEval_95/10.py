def check_dict_case(dictn):
    test_cases = [
        {"a": "apple", "b": "banana"},
        {"a": "apple", "A": "banana", "B": "banana"},
        {"a": "apple", 8: "banana", "a": "apple"},
        {"Name": "John", "Age": "36", "City": "Houston"},
        {"STATE": "NC", "ZIP": "12345"},
        {}
    ]
    expected_results = [
        True,
        False,
        False,
        False,
        True,
        False
    ]
    for d, r in zip(test_cases, expected_results):
        if d == {}:
            if r:
                print("Empty dictionary should return False")
                return False
        elif r:
            if not all(type(k) is str and (k.isupper() or k.islower()) for k in d.keys()):
                print("Invalid dictionary keys")
                return False
        else:
            if all(type(k) is str and (k.isupper() or k.islower()) for k in d.keys()):
                print("Valid dictionary keys but expected False")
                return False
    
    return True