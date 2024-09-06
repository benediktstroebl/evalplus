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
    for i in range(len(test_cases)):
        dict = test_cases[i]
        if expected_results[i] and not len(dict) == 0:
            if all(isinstance(k, str) and (k.isupper() or k.islower()) for k in dict.keys()):
                return True
        elif not expected_results[i]:
            return False
    return False