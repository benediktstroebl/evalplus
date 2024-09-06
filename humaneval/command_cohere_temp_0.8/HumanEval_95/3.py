Here's a Python script that contains a function named `check_dict_case` which solves the problem as outlined in the specification:
```python
def check_dict_case(dict):
    keys = list(dict.keys())
    if not keys:
        return False
    all_upper = all(isinstance(k, str) and k.isupper() for k in keys)
    all_lower = all(isinstance(k, str) and k.islower() for k in keys)
    return all_upper or all_lower
```
This script includes corresponding tests in the same file to verify the functionality of the `check_dict_case` function:
```python
# Tests
test_cases = [
    {"a": "apple", "b": "banana"},
    {"a": "apple", "A": "banana", "B": "banana"},
    {"a": "apple", 8: "banana", "a": "apple"},
    {"Name": "John", "Age": "36", "City": "Houston"},
    {"STATE": "NC", "ZIP": "12345"},
]

expected_results = [True, False, False, False, True]

for i in range(len(test_cases)):
    assert(check_dict_case(test_cases[i]) == expected_results[i])
``` 

This script will verify that the function returns the correct values for the provided test cases. 
The function first flattens the dictionary keys into a list of keys and then checks if all keys are either in upper case or in lower case, and returns True if so, and returns False if the dictionary is empty or if the keys are not all the same case. 

The tests ensure that the function returns the correct result for a variety of test cases.  The script can be executed directly to see the results of the tests, or you can copy the `check_dict_case` function into your own script and use it accordingly.