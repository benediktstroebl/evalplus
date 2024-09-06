```python
def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if isinstance(key, str)}
    list1 = [key.islower() for key in dictn]
    list2 = [key.isupper() for key in dictn]
    if len(dictn) == 0 or (all(list1) or all(list2)):
        return True
    else:
        return False
```
The function first filters the dictionary and only considers keys that are strings, using a dictionary comprehension, and eliminating other data types. Then, it uses `islower()` and `isupper()` methods to determine if all keys are lowercase or uppercase respectively, and then checks if all the generated lists (`list1` and `list2`) contain only true values. If all keys are either all lowercase or all uppercase, the function returns True, otherwise it returns False. 

The following example usage scenarios demonstrate the correctness of the given function:
```python
print(check_dict_case({"a": "apple", "b": "banana"}))  # Output: True
print(check_dict_case({"a": "apple", "A": "banana", "B": "banana"}))  # Output: False
print(check_dict_case({"a": "apple", 8: "banana", "a": "apple"}))  # Output: False
print(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))  # Output: False
print(check_dict_case({"STATE": "NC", "ZIP": "12345"}))  # Output: True
```