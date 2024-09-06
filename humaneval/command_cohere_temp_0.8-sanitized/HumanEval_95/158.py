def check_dict_case(dictn):
    test_cases = [
        {"a":"apple", "b":"banana"}, 
        {"a":"apple", "A":"banana", "B":"banana"}, 
        {"a":"apple", 8:"banana", "a":"apple"}, 
        {"Name":"John", "Age":"36", "City":"Houston"}, 
        {"STATE":"NC", "ZIP":"12345"}
    ]
    
    if not dictn or not isinstance(dictn, dict):
        return False
    elif len(dictn) != len(set(dictn.keys())):
        return False
    else:
        return all(all(isinstance(k, str) and (k == k.upper() or k == k.lower()) for k in dictn.keys()) 
                  for dict in test_cases)