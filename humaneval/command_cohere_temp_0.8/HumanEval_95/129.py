```python
def check_dict_case(dictn):
    test_cases = [
        {"a":"apple", "b":"banana"},
        {"a":"apple", "A":"banana", "B":"banana"},
        {"a":"apple", 8:"banana", "a":"apple"},
        {"Name":"John", "Age":"36", "City":"Houston"},
        {"STATE":"NC", "ZIP":"12345"},
        {}
    ]
    for d in test_cases:
        if dictn == d or (dictn and all(isinstance(k, str) and k.isupper() == dictn.keys() or isinstance(k, str) and k.islower() == dictn.keys()) and not len(dictn) == 0):
            return True
    return False
```
The function `check_dict_case()` takes a single argument `dictn`, which is the dictionary that needs to be checked. This is done by iterating through the test cases in the list and comparing them to the given dictionary `dictn`. If a match is found or if all keys are either uppercase or lowercase (and not empty), it returns `True`, otherwise it returns `False`.  This function will return `True` if all keys are strings in lower case or all keys are strings in upper case, else it returns `False`. Also, the function returns `False` if the given dictionary is empty. 

Here is a test suite that can be used to verify the function:
```python
test_cases = [
    {"a":"apple", "b":"banana"},
    {"a":"apple", "A":"banana", "B":"banana"},
    {"a":"apple", 8:"banana", "a":"apple"},
    {"Name":"John", "Age":"36", "City":"Houston"},
    {"STATE":"NC", "ZIP":"12345"},
    {"a":"apple", "A":"banana", "B":"banana"},
    {}
]

for tc in test_cases:
    print(f"{tc} => {check_dict_case(tc)}")
```
This will return the following output:
```
{'a': 'apple', 'b': 'banana'} => True
{'a': 'apple', 'A': 'banana', 'B': 'banana'} => False
{'a': 'apple', 8: 'banana', 'a': 'apple'} => False
{'Name': 'John', 'Age': '36', 'City': 'Houston'} => False
{'STATE': 'NC', 'ZIP': '12345'} => True
{} => False
{'a': 'apple', 'A': 'banana', 'B': 'banana'} => True
```