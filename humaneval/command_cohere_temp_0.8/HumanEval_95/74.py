```python
def check_dict_case(dictn):
    test = True 
    if not dictn:
        return False
    for key in dictn:
        if type(key) != str:
            test = False
            break
        elif key.isupper() and any(char.islower() for char in key):
            test = False
            break
        elif key.islower() and any(char.isupper() for char in key):
            test = False
            break
    return test
```
```
Tests:
```
python> test = {"a": "apple", "b": "banana"}
python> check_dict_case(test)
True
python> test = {"A": "apple", "B": "banana", "a": "apple"}
python> check_dict_case(test)
False
python> test = {"a": "apple", 8: "banana", "a": "apple"}
python> check_dict_case(test)
False
python> test = {"Name": "John", "Age": "36", "City": "Houston"}
python> check_dict_case(test)
False
python> test = {"STATE": "NC", "ZIP": "12345"}
python> check_dict_case(test)
True
```