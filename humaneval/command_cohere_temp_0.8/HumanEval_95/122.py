```python
def check_dict_case(dictn):
    dictn = {key: val for key, val in dictn.items() if isinstance(key, str)}
    ok = {key.islower() for key in dictn} == {key.isupper() for key in dictn}
    return ok and dictn else False
```
The function first filters the dictionary to contain only strings as keys. Then it checks whether all keys are in lower case or all keys are in upper case using list comprehensions and the `islower` and `isupper` methods. The function returns True if the conditions are met, and False otherwise. The empty dictionary case is also checked. 

Here is a simple test suite that can be used to validate the function:
```python
TESTS = [
    {"dict": {"a": "apple", "b": "banana"}, "result": True},
    {"dict": {"a": "apple", "A": "banana", "B": "banana"}, "result": False},
    {"dict": {"a": "apple", 8: "banana", "a": "apple"}, "result": False},
    {"dict": {"Name": "John", "Age": "36", "City": "Houston"}, "result": False},
    {"dict": {"STATE": "NC", "ZIP": "12345"}, "result": True},
    {"dict": {}, "result": False}
]

for test in TESTS:
    assert check_dict_case(test["dict"]) == test["result"]
``` 
The tests are placed in a array of dictionaries, where each dictionary contains a test case. The `check_dict_case` function is then asserted to return the value contained in the `result` field of the test case dictionary.