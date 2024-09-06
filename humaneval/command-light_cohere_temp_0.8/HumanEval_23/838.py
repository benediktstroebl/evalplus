Here is a self-contained Python script with a function that returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Testing the function
>>> strlen('')
# Should return 0
0

>>> strlen('abc')
# Should return 3
3

>>> strlen('Hello World')
# Should return 11
11

# Additional test with an empty string
>>> strlen('')
# Should return 0
```