```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Testing the function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('123') == 3
    assert strlen('') == 0
    assert strlen('abc123') == 3
```

This script defines a function `strlen` that calculates the length of a given string, and a test function `test_strlen` that ensures the correctness of the `strlen` function with a variety of inputs.  This test after the finaliz just an example of using the `test_strlen` function to validate the `strlen` function.