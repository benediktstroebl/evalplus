```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1
assertEqual(strlen(''), 0)

# Test case 2
assertEqual(strlen('abc'), 3)

# Test case 3
s = "hello"
assert len(strlen(s)) == 5
```