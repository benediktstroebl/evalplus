def check_dict_case(dictn):
    test_cases = [
        {"a": "apple", "b": "banana"},
        {"a": "apple", "A": "banana", "B": "banana"},
        {"a": "apple", 8: "banana", "a": "apple"},
        {"Name": "John", "Age": "36", "City": "Houston"},
        {"STATE": "NC", "ZIP": "12345"},
        {}
    ]
    
    for d in test_cases:
        if len(d) == 0:
            if d == {}:
                return True
            else:
                return False
        else: 
            cm = dict((k, k) for k in d if k != k.lower() and k != k.upper())
            if len(cm) == 0:
                return True
            else: 
                return False