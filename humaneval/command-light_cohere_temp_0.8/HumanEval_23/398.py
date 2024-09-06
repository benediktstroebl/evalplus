```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
assertEqual(strlen(''), 0)
assertEqual(strlen('')), 0,msg="Empty string should return 0")
assertEqual(strlen('abc'), 3)
assertEqual(strlen('abcde'), 6)
assertEqual(strlen(' Sunrise Sunset'), 13)
```