```python
def strlen(string: str) -> int:
    """ Returns length of given string"""
    return len(string)

#Test string length function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('1234') == 4
    assert strlen('') != 4
```
This script defines a function `strlen` that calculates the length of a given string. It then has a test function `test_strlen` which tests the `strlen` function with various input strings.