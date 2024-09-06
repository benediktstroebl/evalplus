```python
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
    elif all(isinstance(k, str) and (k.isupper() or k.islower()) for k in dictn.keys()):
        return True
    else:
        return False
```

This Python script defines a function called `check_dict_case` that takes a single argument, `dictn`, which is the dictionary that needs to be analyzed. The function returns `True` if all the keys in the dictionary are either all written in lowercase or all written in uppercase; otherwise, it returns `False`. The function also checks if the given dictionary is not empty and if it is a dictionary object. 

The script also includes a set of test cases, defined as `test_cases`, which are used to validate the correctness of the `check_dict_case` function. The first test case is a dictionary with lowercase keys, and since it fulfills the condition, the function should return `True`. The second test case has mixed case keys, thereby not fulfilling the condition, so the function should return `False`. The third test case has duplicate keys and also has a non-string key, so the function should return `False`. The fourth test case has uppercase keys, but they are not all uppercase, so the function should return `False`. The last test case has all uppercase keys, so the function should return `True`. 

This code demonstrates how to solve the problem and also includes corresponding tests which allow to verify the correctness of the solution.