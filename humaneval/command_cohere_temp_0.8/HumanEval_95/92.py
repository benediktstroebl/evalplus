Here's a Python script that contains a function `check_dict_case` which solves the problem as described in the provided markdown code block:
```python
def check_dict_case(dict):
    if not dict:
        return False
    keys = list(dict.keys())
    # Check if all keys are lowercase
    if all(isinstance(key, str) and key.islower() for key in keys):
        return True
    # Check if all keys are uppercase
    if all(isinstance(key, str) and key.isupper() for key in keys):
        return True
    return False

# Example usage
ex_dicts = [
    {"a": "apple", "b": "banana"},
    {"a": "apple", "A": "banana", "B": "banana"},
    {"a": "apple", 8: "banana", "a": "apple"},
    {"Name": "John", "Age": "36", "City": "Houston"},
    {"STATE": "NC", "ZIP": "12345"},
]

for ex_dict in ex_dicts:
    print(f"{check_dict_case(ex_dict)}")
```

This script will output:
```bash
True
False
False
False
True
```

The function first checks if the dictionary is empty, and if so, returns `False`. It then checks if all keys are lowercase or all keys are uppercase. The `all` function is used in combination with a generator expression to check all keys in the dictionary. The function returns `True` if all keys satisfy either of the two conditions; otherwise, it returns `False`. The examples demonstrate the behavior of the function on different types of dictionaries as described in the problem statement.