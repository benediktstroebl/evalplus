```python
def strlen(string: str) -> int:
    """ Returns length of given string """
    return len(string)

# Testing the function
>>> strlen('')
0
>>> strlen('abc')
3
>>> strlen('')aaa')
Error: ValueError: '>' cannot convert item to str'
```