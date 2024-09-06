```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test the function with various inputs
>>> strlen('')
0
>>> strlen('abc')
3
>>> strlen('')abc')
3
>>> strlen('   ')
3
>>> strlen(' '''')
6
>>> strlen('	')
4
>>> strlen(' bar')
3

I hope this function will always return the length of the passed string, which is a fundamental string operation!