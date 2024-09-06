```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
assertEqual(strlen(''), 0)
assertEqual(strlen('')), 0, msg="Should return 0 for an empty string"
assertEqual(strlen('abc')), 3, msg="Should return 3 for 'abc'"
assertEqual(strlen('abcde'), 6, msg="Should return 6 for 'abcde'")
assertEqual(strlen(' '), 0, msg="Should return 0 for space")
assertEqual(strlen(""), 0, msg="Should return 0 for single space")
```