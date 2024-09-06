Here's a Python script that contains a function named `check_dict_case` which solves the problem as per the given markdown code block:
```python
def check_dict_case(dict):
    if not dict:
        return False
    
    all_upper = all(isinstance(key, str) and key.isupper() for key in dict.keys())
    all_lower = all(isinstance(key, str) and key.islower() for key in dict.keys())
    return all_upper or all_lower
```
This code defines a function named `check_dict_case` that takes in a dictionary as an argument and checks if all the keys therein are either all in upper case or all in lower case, returning a boolean value accordingly.

The above solution is self-contained and should work well for the problem described in the markdown code block. Let's go through the steps one by one:
1. At first, we handle the edge case of an empty dictionary or `None` dictionary since the purpose of this function is to check if all keys in the dictionary are of the same case (either all upper case or all lower case). To achieve this we use the `if not dict:` statement which directly returns `False` if the dictionary is empty.
2. After that, we use two nested `all()` functions to check if all keys in the dictionary are either all in upper case or all in lower case. The `all()` function returns `True` if all elements of the iterable are true. In our case, for the upper case condition, we use `key.isupper()` for each key in the dictionary, and for the lower case condition, we use `key.islower()` for each key in the dictionary.
3. Finally, we return `True` if either of these conditions is true, indicating that all keys are of the same case, and `False` otherwise.

The `check_dict_case` function utilizes built-in Python functionalities, namely `isupper()`, `islower()`, and `all()`, to achieve the desired result and conform to the problem description provided. The function should handle all the test cases mentioned in the provided markdown code block. 

You can use this code to test your function and solve the problem. Feel free to adapt this solution to your needs. If this solution addresses your problem, please let me know if I can assist you with anything else!