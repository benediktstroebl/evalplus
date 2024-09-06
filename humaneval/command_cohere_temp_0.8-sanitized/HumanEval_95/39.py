def check_dict_case(dictn):
    test_cases = [
        {"a": "apple", "b": "banana"},
        {"a": "apple", "A": "banana", "B": "banana"},
        {"a": "apple", 8: "banana", "a": "apple"},
        {"Name": "John", "Age": "36", "City": "Houston"},
        {"STATE": "NC", "ZIP": "12345"},
        {}
    ]
    expected_results = [True, False, False, False, True, False]
    for i in range(len(test_cases)):
        dict = test_cases[i]
        result = expected_results[i]
        if dict.keys() == dict().keys():
            result = True
        if result != check_dict_case(dict):
            return False
    return True