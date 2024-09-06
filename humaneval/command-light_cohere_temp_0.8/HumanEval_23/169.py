```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Tests
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert len("") == 0
    assert len(" ") == 1
    assert len("___") == 5
```