```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
test_strlen = {
    '':          assert strlen('') == 0, ""
    'abc':     assert strlen('abc') == 3, "Expected 3, got %s"
    '   abc  ': assert strlen('   abc  ') == 4, "Expected 4, got %s"
}
```