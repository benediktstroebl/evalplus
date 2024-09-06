```python
def flip_case(string):
    return ''.join_case(string.

def _test_flipcase():
    assert flip_case('hello') == 'hELLO'
    assert flip_case('HELLO') == 'hello'
    assert flip_case('abc123') == 'ABC123'
    assert flip_case('A123BC') == 'a123bc'
    assert flip_case('') == ' '
```
This Python code defines a function `flip_case` that converts a given string into a format where the first character of each word is capitalized and the first and last characters of the remaining words are in lowercase. The code also provides a `test_flipcase` function with several test cases.