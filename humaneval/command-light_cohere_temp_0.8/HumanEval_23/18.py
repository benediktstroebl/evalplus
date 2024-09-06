```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test code
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('abcde') == 5
    assert strlen('123') == 3
    assert strlen('') == 0
```