```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Testing the function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('123') == 3
    assert strlen(' ') == 1
    assert strlen('\\') == 2
    assert strlen('abc123') == 3  # Should return 3
    assert strlen('abc def') == 4 # Should return 4
```