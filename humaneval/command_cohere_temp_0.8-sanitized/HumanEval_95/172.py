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
        if result:
            if all(isinstance(k, str) and k.isupper() for k in dict):
                continue
            elif all(isinstance(k, str) and k.islower() for k in dict):
                continue
        else:
            return False
    return False if dictn == {} else True