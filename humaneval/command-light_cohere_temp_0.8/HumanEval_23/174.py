```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

#Test string length function
test_strlen = [
    assert strlen('') == 0, "Should return 0 for an empty string"
    assert strlen('abc') == 3, "Should return 3 for 'abc'"
]
```