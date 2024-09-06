```python
def strlen(string: str) -> int:
    return len(string)

# Testing the function with valid inputs
assertEqual(strlen(''), 0)
assertEqual(strlen(' ')), 3
assertEqual(strlen('abc')), 3
assertEqual(strlen('abc123')), 5

# Testing the function with invalid inputs (none)
assertNotEqual(strlen(None)), ZeroDivisionError
assertNotEqual(strlen(''')), ZeroDivisionError
assertNotEqual(strlen([])), AssertionError
```