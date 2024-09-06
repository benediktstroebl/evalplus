```python
def strlen(string: str) -> int:
    """ Returns length of the given string """
    return len(string)

# Tests
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('') != 0
```