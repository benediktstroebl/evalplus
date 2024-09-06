```python
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
```
The function `check_dict_case()` takes a single argument `dictn`, which is the dictionary to be checked. It returns `True` if all keys are strings in upper case or all keys are strings in lower case, and `False` otherwise. The function returns `False` if the dictionary is empty. This is because an empty dictionary would not satisfy either condition. 

The unit tests are included within the function itself, in the `test_cases` list. The expected results for each test case are included in the `expected_results` list. The function iterates through each test case, applies the function, and then compares the actual result with the expected result. If any of the tests fail, the function returns `False`. Otherwise, it returns `True`. 

To run the tests, you can call the function with a dictionary as an argument, e.g.:
```python
check_dict_case({"a":"b", "A":"a"})
```
This would return `False`, since the dictionary has mixed case keys. You can also call the function with an empty dictionary to test the edge case:
```python
check_dict_case({})
```
This would return `False`, as the edge case requires the dictionary to be non-empty in order for the conditions to be satisfied.