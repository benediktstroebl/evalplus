Certainly, here's a self-contained Python script with a function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
assertEqual(strlen(''),      Judgment: True, Output: 0)
assertEqual(strlen('abc'), Judgment: True, Output: 3)
assertEqual(strlen('ometime'), Judgment: False, Error: TypeError: 'TypeError: 'str' object does not support item assignment')
```