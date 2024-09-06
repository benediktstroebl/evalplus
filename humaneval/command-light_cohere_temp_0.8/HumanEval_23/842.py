```python
def strlen(string: str) -> int:
    """ Returns length of the given string."""
    return len(string)

# Testing the function
>>> strlen('')
0
>>> strlen('abc')
3
>>> strlen('')abc')
3
>>> strlen('abcabc')
4
>>> strlen('     ')
6
>>> strlen('123')==3
True
```