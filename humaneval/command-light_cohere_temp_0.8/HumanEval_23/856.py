Here is a self-contained Python script that defines a function `strlen` which calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    Returns length of the string
    """
    return len(string)

# Test the function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
```