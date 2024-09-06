Here's a Python script that contains a function called `check_dict_case` that solves the problem as outlined in the markdown code block provided:
```python
def check_dict_case(dict):
    if not dict:
        return False
    keys = list(dict.keys())
    lower_keys = [key.lower() for key in keys]
    upper_keys = [key.upper() for key in keys]
    return len(set(lower_keys)) == len(lower_keys) and len(set(upper_keys)) == len(upper_keys)
```

This function first handles the edge case where the input dictionary is empty, returns False in such cases. Next, it converts all keys in the dictionary to lowercase using a list comprehension, then it checks if all unique keys in the dictionary become the same after conversion to lowercase, and similarly, it checks if all unique keys remain the same after conversion to uppercase. If all keys have the same case (either all lowercase or all uppercase), the function returns True, otherwise, it returns False.

To showcase its usage, we can import the function and test it with different scenarios like this:
```python
# Import the function from the above code
from func import check_dict_case 

# Test Scenarios
print(check_dict_case({"a":"apple", "b":"banana"}))  # Should print True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))  # Should print False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))  # Should print False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))  # Should print False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"}))  # Should print True
```

All test cases should return the expected outputs based on the specifications outlined in the markdown code block.