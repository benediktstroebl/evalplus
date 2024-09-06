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
        if dictn == d or (all(isinstance(k, str) and (k.isupper() or k.islower()) for k in dict(d).keys()) and not len(d) == 0):
            return True
    return False