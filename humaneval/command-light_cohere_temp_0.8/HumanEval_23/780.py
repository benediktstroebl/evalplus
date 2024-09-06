```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns: The length of the string in Unicode code units
        Raises: ValueError if the string is empty"""

    if not string:
        raise ValueError('Input string is empty')

    return len(string)

# Tests
assertEqual(strlen(''), 0)
assertEqual(strlen(' ')), 1
assertEqual(strlen('abc')), 3
assertEqual(strlen(' sut Jana Rosa! ')), 11
```