Here is a self-contained Python script that solves the problem of calculating the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Testing the function
>>> strlen('')
0

>>> strlen('abc')
3

>>> strlen('iability')
5
```