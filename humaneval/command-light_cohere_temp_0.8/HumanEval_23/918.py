```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Test the function with various strings
>>> strlen('')
0
>>> strlen('abc')
3
>>> strlen('')abc')
3
>>> strlen('	')
3
>>> strlen(' 123')
4
>>> strlen('abcdefgh')
11
```