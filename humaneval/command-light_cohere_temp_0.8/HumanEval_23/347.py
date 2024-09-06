```python
def strlen(string: str) -> int:
    return len(string)

# Test code
assertEqual(strlen(''), 0)
assertEqual(strlen(' ')), 1  # space is character
assertEqual(strlen('abc')), 3  # 'abc' has 3 characters
assertEqual(strlen('abcde')), 3  # Added additional test case
assertEqual(strlen('raining'), 8)
```