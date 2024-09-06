```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test the function
>>> strlen('')
0
>>> strlen('abc')
3
>>> strlen('')abc')
Error: TypeError: 'str' object does not support item assignment 

# Substitute the function and pass the test! 
def __starting_point():
    return strlen('')abc')  # ValueError: 'abc' object does not support item assignment