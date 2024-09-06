```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns length of the string passed as parameter
        """
    assert isinstance(string, str), f"Input should be a string, but got {type(string)}"
    return len(string)

# Example test cases
assertEqual(strlen(''), 0)
assertEqual(strlen('abc'), 3)
assertEqual(strlen('abcabc'), 6)
assertEqual(strlen(''), -1)
```