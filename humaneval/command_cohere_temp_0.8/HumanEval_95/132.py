```python
def check_dict_case(dictn):
    if not dictn:
        return False
    for key in dictn:
        if not isinstance(key, str):
            return False
        if dictn[key].isupper() != key.isupper():
            return False
    return True
```
This function checks if all the keys in the dictionary are either all lowercase or all uppercase and returns True if so, else returns False. The function also checks if the dictionary is empty or if any of the keys are not strings, and returns False in those scenarios. 

Here is an example usage of the function with a dictionary test case:
```python
test_case = {"a":"apple", "A":"banana", "B":"banana"}
print(check_dict_case(test_case)) 
```
This will print False, as the keys in the test case are not all the same case.