```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns 0 if the string is empty """
    return len(string) if string else 0

# Test cases
>>> strlen('')
0

>>> strlen('abc')
3

>>> strlen('')abc')
3

>>> strlen('abcabc')
4

>>> strlen('abc') < strlen('abcabc')
True
```