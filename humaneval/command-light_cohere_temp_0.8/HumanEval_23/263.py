```python
def strlen(string: str) -> int:
    """ Returns length of given string."""
    return len(string)

# Test cases
assertEqual(strlen(''), 0)
assertEqual(strlen('abc'), 3)
assertEqual(strlen('')), 0)
assertEqual(strlen('  '), 3)
assertEqual(strlen('\t'), 6)
assertEqual(strlen('abcde'), 7)

# Sample usage
print(strlen(''))
print(strlen('abc'))
```