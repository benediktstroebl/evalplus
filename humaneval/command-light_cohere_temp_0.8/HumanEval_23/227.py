```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns 0 if the string is empty """
    if not string:
        return 0
    return len(string)

# Test the function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('        ') == 3  # Extra spaces are counted too
    assert strlen('abcABC') == 3  # Capital letters are counted too
    assert strlen('') == 0
```