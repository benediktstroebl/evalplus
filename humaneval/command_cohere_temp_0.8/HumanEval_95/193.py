Here's a Python script that contains a function, `check_dict_case`, which takes a dictionary as an argument and returns True if all keys either are lowercase strings or uppercase strings, and returns False otherwise. The script also includes test cases to ensure the function behaves as expected:
```python
def check_dict_case(dict):
    if not dict:
        return False
    keys = list(dict.keys())
    all_lower = all(isinstance(k, str) and k.islower() for k in keys)
    all_upper = all(isinstance(k, str) and k.isupper() for k in keys)
    return all_lower or all_upper

# Test Cases
assert check_dict_case({"a": "apple", "b": "banana"}) == True
assert check_dict_case({"a": "apple", "A": "banana", "B": "banana"}) == False
assert check_dict_case({"a": "apple", 8: "banana", "a": "apple"}) == False
assert check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}) == False
assert check_dict_case({"STATE": "NC", "ZIP": "12345"}) == True
```

This script will give you a function that solves the problem as outlined in the prompt, and the tests ensure it works correctly for the use cases provided. 

You can use this code to verify your solution or explore how you can solve this problem.