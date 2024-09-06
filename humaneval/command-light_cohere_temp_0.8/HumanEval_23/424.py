```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
assertEqual(strlen(''),   0)
assertEqual(strlen('abc'), 3)
assertEqual(strlen('']), 3)
assertEqual(strlen([]), 0)
assertEqual(strlen('123'), 5) # Integer overflow case

# These additional tests cover various edge cases to ensure the function works correctly.