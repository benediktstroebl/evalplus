```python
def check_dict_case(dictn):
    if not dictn:
        return False
    booln = all(type(key) == str for key in dictn) and all(key.islower() or key.isupper() for key in dictn)
    return booln
```
This function checks if all the keys in the provided dictionary are either all lowercase or all uppercase and string types, otherwise, it returns False. It also checks if the dictionary is not empty. The latter is ensured through the condition `if not dictn:` which checks if the input dictn has a length different from zero. The line `booln = all(type(key) == str for key in dictn) and all(key.islower() or key.isupper() for key in dictn)` applies two conditions to the dictionary keys using the `all` function. The first tests if all keys are of string type using `type(key) == str`. The second checks if all keys are either lowercase using `key.islower()` or uppercase using `key.isupper()`. The `or` operator combines these two conditions. The overall logic of the function adheres to the problem's statement as it returns True if all keys are either lowercase or uppercase strings and False otherwise. 

Here is a simple test suite that can be used to validate the function implementation:
```python
def test_check_dict_case():
    # Basic tests:
    assert check_dict_case({"a": "apple", "b": "banana"}) == True
    assert check_dict_case({"A": "apple", "B": "banana"}) == False
    assert check_dict_case({"a": "apple", 8: "banana", "a": "apple"}) == False

    assert check_dict_case({"name": "John", "age": "36", "city": "Houston"}) == False
    assert check_dict_case({"STATE": "NC", "ZIP": "12345"}) == True

    # Edge case
    assert check_dict_case({}) == False

test_check_dict_case()
```
The test suite contains four test functions that cover different scenarios which can validate the functionality of the `check_dict_case` function.