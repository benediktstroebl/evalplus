```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns 0 if the string is empty"""
    if not string:
        return 0
    return len(string)

# Test cases
assertEqual(strlen(''), 0)
assertEqual(strlen('abc')), 3
assertEqual(strlen('abcabc')), 6)
assertEqual(strlen(' abc  ')), 5
assertEqual(strlen('')) , 0

```
This code defines a function `strlen` that calculates the length of a given string, returning 0 if the input is an empty string. The test cases ensure the