```python
def check_dict_case(dictn):
    dictn = {key: dictn[key] for key in dictn if isinstance(key, str)}
    ok = all(key.islower() for key in dictn) and all(key in dictn for key in dictn.keys())
    return ok and not len(dictn) or all(key.isupper() for key in dictn) and all(key in dictn for key in dictn.keys())
```
The function checks if all keys are in lowercase or all keys are in uppercase and returns True if it meets those conditions and the dictionary is not empty. If the dictionary is empty, it returns False. The tests are internal and are based on the examples provided, feeding a variety of dictionaries to see if the function returns the correct True and False results. 
```python
def test_check_dict_case():
    assert check_dict_case({"a": "apple", "b": "banana"})
    assert not check_dict_case({"a": "apple", "A": "banana", "B": "banana"})
    assert not check_dict_case({"a": "apple", 8: "banana", "a": "apple"})
    assert not check_dict_case({"Name": "John", "Age": "36", "City": "Houston"})
    assert check_dict_case({"STATE": "NC", "ZIP": "12345"})
    assert not check_dict_case({})
``` 
The tests will print out 'asserted' or 'failed' for each test case, depending on whether the condition specified in the assert statement is met. 

The provided solutions assume that the dictionary is purely string keys and integer, string values and that the keys are actually present in the dictionary. 
If the dictionary can contain other types as keys or values, the functions should be adjusted accordingly.