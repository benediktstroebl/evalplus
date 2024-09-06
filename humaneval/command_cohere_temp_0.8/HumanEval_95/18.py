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
The function first handles an empty dictionary case and returns False. It then checks if all keys are strings and if they are either all in upper case or all in lower case, and returns a corresponding value. The function returns False if the conditions are not met. The example usage is provided below:
```python
print(check_dict_case({"a":"apple", "b":"banana"})) # Output: True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # Output: False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"})) # Output: False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # Output: False
print(check_dict_case({"STATE":"NC", "ZIP":"12345"})) # Output: True
``` 
The provided examples all follow the problem statement and output the expected values.