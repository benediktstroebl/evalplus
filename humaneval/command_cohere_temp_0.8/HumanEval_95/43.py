```python
def check_dict_case(dictn):
    keys = []
    for key in dictn.keys():
        keys.append(key)
    if len(keys) == 0:
        return False
    elif all(isinstance(key, str) and (key.isupper() or key.islower()) for key in keys):
        return True
    else:
        return False
```
The function first handles an empty dictionary case and returns False. Then, it checks whether all keys are strings and all keys are in upper case or lower case. The `all` function is used to efficiently check the conditions for all keys in the dictionary. 
The following unit tests are also included:
```python
test_cases = [
    {'dict': {'a': 'apple', 'b': 'banana'}, 'expected': True},
    {'dict': {'a': 'apple', 'A': 'banana', 'B': 'banana'}, 'expected': False},
    {'dict': {'a': 'apple', 8: 'banana', 'a': 'apple'}, 'expected': False},
    {'dict': {'Name': 'John', 'Age': '36', 'City': 'Houston'}, 'expected': False},
    {'dict': {'STATE': 'NC', 'ZIP': '12345'}, 'expected': True}
]

for case in test_cases:
    assert(check_dict_case(case['dict']) == case['expected'])
```

The tests will check various cases to ensure the `check_dict_case` function behaves as expected.