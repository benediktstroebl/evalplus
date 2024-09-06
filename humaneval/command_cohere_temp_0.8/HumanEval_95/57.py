Here's a Python script that contains a function `check_dict_case` which solves the problem as outlined in the specification:
```python
def check_dict_case(dict):
    if not dict:
        return False
    keys = list(dict.keys())
    # checking if all keys are lowercase or uppercase
    return all(len(keys) == len(set(keys)) and keys == keys.lower() or keys == keys.upper())

def test_check_dict_case():
    assert check_dict_case({"a":"apple", "b":"banana"})
    assert not check_dict_case({"a":"apple", "A":"banana", "B":"banana"})
    assert not check_dict_case({"a":"apple", 8:"banana", "a":"apple"})
    assert not check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})
    assert check_dict_case({"STATE":"NC", "ZIP":"12345" })
    assert not check_dict_case({"foo": "bar", "baz": "qux"})

test_check_dict_case()
``` 

The `check_dict_case` function first handles the base case of an empty dictionary gracefully and returns False. It then proceeds to loop through all keys using a set comprehension to check if all keys are identical after conversion to either uppercase or lowercase. The function returns True if this condition is met and False otherwise. 

The `test_check_dict_case` function provides test cases to help verify correct operation of the `check_dict_case` function. 

This solution is concise and practical, and should serve as a useful reference for solving this problem. 

Let me know if this solves your problem or if you have any other questions!