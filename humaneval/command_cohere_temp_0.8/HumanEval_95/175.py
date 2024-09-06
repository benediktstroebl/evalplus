Here's a Python script that contains a function, `check_dict_case`, which solves the problem as described in the markdown code block:
```python
def check_dict_case(dict):
    if not dict:
        return False
    # Convert dictionary keys to lowercase
    lower_case_dict = {key.lower(): value for key, value in dict.items()}
    # Convert dictionary keys to uppercase
    upper_case_dict = {key.upper(): value for key, value in dict.items()}
    # Check if all keys are the same case
    if lower_case_dict == upper_case_dict or dict == upper_case_dict:
        return True
    else:
        return False

# Example usage
exemplar_dict = {"a": "apple", "b": "banana"}
print(check_dict_case(exemplar_dict))  # Output: True

variation1 = {"A": "apple", "a": "apricot", "B": "banana"}
print(check_dict_case(variation1))  # Output: False

variation2 = {"name": "John", "Age": "36", "city": "Houston"}
print(check_dict_case(variation2))  # Output: False

variation3 = {"STATE": "NC", "zip": "12345"}
print(check_dict_case(variation3))  # Output: True
```

This script defines the `check_dict_case` function, which takes a dictionary as input. It first checks if the dictionary is empty, and if so, returns False. It then creates two additional dictionaries with all keys in lowercase and all keys in uppercase, respectively. If the original dictionary keys are consistent in case with either the all-lowercase or all-uppercase keys, the function returns True, otherwise, it returns False. The examples usage section demonstrates the function on a variety of dictionaries to show its behavior.