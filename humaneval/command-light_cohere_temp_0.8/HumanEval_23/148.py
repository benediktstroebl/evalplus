```python
def strlen(string: str) -> int:
    """ Returns length of the given string."""
    return len(string)

# Test cases
assertEqual(strlen(''),            # Should return 0: empty string
)
assertEqual(strlen('abc')          # Should return 3:  'abc' has 3 characters
)
assertEqual(strlen('abcabc')        # Should return 6: 'abcabc' has 6 characters
)
assertEqual(strlen('') == 0,        # Should return True: empty string is 0
)
assertEqual(strlen('A') == 1,        # Should return True: 'A' has 1 character
)(NEVER_INF)
```