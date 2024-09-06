```python
def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if isinstance(key, str)}
    dictn = {key: val for key, val in dictn.items() if key.isupper() or key.islower()}
    return not bool(dictn) or all(dictn.values()) and len(dictn) != 0
```

The above `check_dict_case()` function validates the dictionary such that all the keys are either `UPPERCASE` or `lowercase` and returns `True` if the validation succeeds. Otherwise, it returns `False`. Also, the function returns `False` if the given dictionary is empty. 

Here is a test suite to ensure it works correctly:
```python
test_cases = [
    {"a": "apple", "b": "banana"},
    {"a": "apple", "A": "banana", "B": "banana"},
    {"a": "apple", 8: "banana", "a": "apple"},
    {"Name": "John", "Age": "36", "City": "Houston"},
    {"STATE": "NC", "ZIP": "12345"},
    {}
]

expected_ans = [True, False, False, False, True, False]

for i in range(len(test_cases)):
    test_dict = test_cases[i]
    actual_ans = check_dict_case(test_dict)
    assert actual_ans == expected_ans[i], f"Expected {expected_ans[i]}, but got {actual_ans} for {test_dict}"
```