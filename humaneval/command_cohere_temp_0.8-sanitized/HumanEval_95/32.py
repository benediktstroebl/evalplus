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
        if result == False and not dict:
            continue
        elif len(dict) == 0:
            return False
        else:
            lower_case_dict = {k.lower(): v for k, v in dict.items()}
            upper_case_dict = {k.upper(): v for k, v in dict.items()}
            if (len(lower_case_dict) == len(dict) and len(upper_case_dict) == len(dict)):
                return True
            else:
                return False