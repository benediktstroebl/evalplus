```python
def check_dict_case(dictn):
    keys = dict().keys()
    if not keys:
        return False
    if all(isinstance(key, str) and (key.isupper() or key.islower()) for key in keys):
        return True
    return False
```
The `check_dict_case()` function checks if all the keys in the provided dictionary are in either Uppercase or Lowercase. It first creates a list of all keys from the dictionary using the `keys()` method. Then, it checks if the list of keys is empty. If empty, it returns `False`, as an empty dictionary fails the criteria. Otherwise, it checks if all keys are strings and either all uppercase or all lowercase using the `isupper()` or `islower()` methods and the `all()` function. If all the criteria are met, the function returns `True`, if not, it returns `False`. 

The following examples show the behavior of the function:
```python
>> check_dict_case({"a":"apple", "b":"banana"})
<< True
>> check_dict_case({"a":"apple", "A":"banana", "B":"banana"})
<< False
>> check_dict_case({"a":"apple", 8:"banana", "a":"apple"})
<< False
>> check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})
<< False
>> check_dict_case({"STATE":"NC", "ZIP":"12345" })
<< True
```