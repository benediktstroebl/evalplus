```python
def check_dict_case(dictn):
    dictn = {key: value for key, value in dictn.items() if isinstance(key, str)}
    return len(dictn) == 0 or (all(key.isupper() for key in dictn) or all(key.islower() for key in dictn))
```
This function checks if all the keys in the provided dictionary are either all in upper case or all in lower case. It also handles the edge case where the given dictionary is empty. The corresponding unit tests are also included to verify the correctness of the function. 
```python
def test_check_dict_case():
    # Dictionary with mixed case keys
    mixed_case_dict = {'a': 'apple', 'A': 'banana', 'B': 'banana'}
    assert check_dict_case(mixed_case_dict) == False

    # Dictionary with all upper case keys
    upper_case_dict = {'STATE': 'NC', 'ZIP': '12345'}
    assert check_dict_case(upper_case_dict) == True

    # Dictionary with all lower case keys
    lower_case_dict = {'name': 'John', 'age': '36', 'city': 'Houston'}
    assert check_dict_case(lower_case_dict) == False

    # Empty dictionary
    empty_dict = {}
    assert check_dict_case(empty_dict) == True

    # Dictionary with a mix of upper and lower case keys and values
    mixed_case_dict = {'name': 'John', 'Age': '36', 'city': 'Houston', 'stateId': '45'}
    assert check_dict_case(mixed_case_dict) == False

test_check_dict_case()
``` 
The tests will exercise the function with a variety of input dictionaries, including empty dictionaries, dictionaries with a mix of uppercase and lowercase keys, and dictionaries with all uppercase or all lowercase keys. 
This way, you can confidently determine if the function works as expected. 
Feel free to modify the function and tests to suit your specific requirements or to handle additional edge cases if needed.