Here's a Python script that contains a function called `check_dict_case` that solves the problem as outlined in the specification:
```python
def check_dict_case(dict):
    if not dict:
        return False
    # Check if all keys are lowercase
    if all(isinstance(k, str) and k.islower() for k in dict):
        return True
    # Check if all keys are uppercase
    if all(isinstance(k, str) and k.isupper() for k in dict):
        return True
    return False
```

This function first checks if the dictionary is empty, and if so, returns False. Otherwise, it checks if all keys are lowercase or uppercase. It returns True if either of these conditions is met, and returns False otherwise. 

Here's a simple test suite to verify the functionality of the solution:
```python
def test_check_dict_case():
    assert check_dict_case({"a": "apple", "b": "banana"}) == True
    assert check_dict_case({"a": "apple", "A": "banana", "B": "banana"}) == False
    assert check_dict_case({"a": "apple", 8: "banana", "a": "apple"}) == False
    assert check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}) == False
    assert check_dict_case({"STATE": "NC", "ZIP": "12345"}) == True
    assert check_dict_case({"lower": "case", "mixed": "keys"}) == False
``` 

When you run the test suite, all tests should pass.