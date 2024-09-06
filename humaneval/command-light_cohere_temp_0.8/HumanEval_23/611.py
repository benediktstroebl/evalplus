```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns length of string
        """
    assert isinstance(string, str), f"Input must be a string, not {type(string)}"
    assert len(string) == strlen(string), f"Length of string must be equal to itself, got {len(string)} != {strlen(string)}"
    return strlen(string)

# Example test cases
assertEqual(strlen(''), 0)
assertEqual(strlen('abc'), 3)
assertEqual(strlen('abcdef'), 6)
assertEqual(strlen(''), 0)
assertEqual(strlen([]), 0)
assertNotEqual(strlen('abcde'), 6)
```