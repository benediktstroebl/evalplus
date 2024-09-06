Here is a self-contained Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
assertEqual(strlen(''),       0)
assertEqual(strlen('abc')), 3
assertEqual(strlen('abcde')) 

# assertEqual(strlen(' '), 0) # empty string
assertNotEqual(strlen(''), 4)  # not empty
```