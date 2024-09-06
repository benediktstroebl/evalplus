```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test the function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('') == 0
```