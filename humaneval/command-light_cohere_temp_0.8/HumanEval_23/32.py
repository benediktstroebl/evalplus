Here is a self-contained Python script that defines a function strlen that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test the function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
``` 
This script provides a function `strlen`, which takes a string as input and returns its length. It then provides a the test case, ensuring the function behaves correctly with empty and non-empty strings.