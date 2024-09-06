```python
def check_dict_case(dictn):
    if not dictn:
        return False
    for key in dictn:
        if not isinstance(key, str):
            return False
        elif key.isupper() and any(c.islower() for c in key):
            return False
        elif key.islower() and any(c.isupper() for c in key):
            return False
    return True
```
This function checks if all the keys in the dictionary are in lowercase or uppercase, and returns True if so, else returns False. It also checks for any keys that are strings but not all lowercase or all uppercase. The empty dictionary case is also checked. 

Here is a markdown code block with corresponding test cases to verify the correct functionality of the function:
```python
def test_check_dict_case():
    assert check_dict_case({"a": "apple", "b": "banana"})
    assert not check_dict_case({"a": "apple", "A": "banana", "B": "banana"})
    assert not check_dict_case({"a": "apple", 8: "banana", "a": "apple"})
    assert not check_dict_case({"Name": "John", "Age": "36", "City": "Houston"})
    assert check_dict_case({"STATE": "NC", "ZIP": "12345"})
    assert not check_dict_case({"a": "apple", "b": "banana", "c": "cherry"})
    assert check_dict_case({})
```

You can copy and paste this code into a Python environment or IDE of your choice to test the function and verify its correctness against these specific test cases. Feel free to add more tests as needed to cover other corner cases.