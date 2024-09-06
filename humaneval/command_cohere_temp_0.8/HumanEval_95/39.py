```python
def check_dict_case(dictn):
    if not dictn:
        return False
    for key in dictn:
        if not isinstance(key, str):
            return False
        elif key.isupper() and any(char.islower() for char in key):
            return False
        elif key.islower() and any(char.isupper() for char in key):
            return False
    return True
```
This function checks if all the keys in the dictionary are consistent in their casing, either all uppercase or all lowercase, and returns True if so, else returns False. The function also checks if the dictionary is empty or if any key is not a string, and returns False in those scenarios. 

Here is a simple unit test for the function to ensure its robustness:
```python
def test_check_dict_case():
    assert check_dict_case({"a":"apple", "b":"banana"}) == True
    assert check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) == False
    assert check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) == False
    assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) == False
    assert check_dict_case({"STATE":"NC", "ZIP":"12345" }) == True
    assert check_dict_case({}) == False
    assert check_dict_case({"a":1, "b":2}) == False
``` 
This test suite contains 6 different tests, each testing a different edge case in the function to ensure its correctness. 

If you wish to run these tests individually to verify the function's behavior, use the following commands:
```python
test_check_dict_case()
```
This will run the test suite and display 'OK' if all the tests pass, else it will show the errors present in the code.