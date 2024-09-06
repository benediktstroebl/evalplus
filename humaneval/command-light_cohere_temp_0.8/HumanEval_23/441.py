Here is a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
test_strlen = unittest.TestCase(['', 'abc'])
test_strlen.result = [3]
```