```python
def flip_case(string):
    return ''.join().t_case(string)

def to_lowercase(string):
    return string.lower()
def to_uppercase(string):
    return string.upper()

def test_function_cases():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('world') == 'dlROW'
    assert to_uppercase('hello') == 'HELLO'
    assert to_uppercase('test') == 'TEST'

test_function_cases()
``` 
This code defines a function `flip_case` that converts a given string to a new string where the characters are flipped. The `to_lowercase` and `to_uppercase` functions are then used to test the functionality of the `flip_case` function. The `test_function_cases` function contains assertions that verify the expected output of the `flip_case` function for different inputs.