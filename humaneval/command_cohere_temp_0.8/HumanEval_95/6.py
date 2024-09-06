Here's a Python script that contains a function, `check_dict_case`, which takes a dictionary as an argument and returns True if all keys either are lowercase strings or are uppercase strings, and returns False otherwise. The script also includes test cases to verify the functionality of the function:
```python
def check_dict_case(dict):
    if not dict:
        return False 
    all_lower = all(isinstance(key, str) and key.islower() for key in dict)
    all_upper = all(isinstance(key, str) and key.isupper() for key in dict)
    return all_lower or all_upper

# Test Cases
assert check_dict_case({"a": "apple", "b": "banana"}) == True
assert check_dict_case({"a": "apple", "A": "banana", "B": "banana"}) == False
assert check_dict_case({"a": "apple", 8: "banana", "a": "apple"}) == False
assert check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}) == False
assert check_dict_case({"STATE": "NC", "ZIP": "12345"}) == True
```

This script includes the function `check_dict_case`, which examines whether all keys in the provided dictionary are either in lowercase or in uppercase. The function initially checks if the dictionary is empty, and if so, it returns False. It then iterates through the keys in the dictionary, checking if all keys are either lowercase or uppercase. The function returns True if all keys match either criterion, and False otherwise.

The script also uses the `assert` statement to test the function with specific dictionaries. These test cases represent different scenarios in order to confirm that the function behaves as expected. You can add more test cases to cover a variety of scenarios and ensure the robustness of the function.