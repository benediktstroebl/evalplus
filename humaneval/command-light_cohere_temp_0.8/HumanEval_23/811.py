```python
def strlen(string: str) -> int:
    return len(string)

# Testing the function
>>> strlen('')
0

>>> strlen('abc')
3

>>> strlen(' ' * 'abc' )
6

>>> strlen('abc123')
7
``` 
This code defines a function `strlen` that calculates the length of a given string. The function uses the basic Python's `len()` function to get the length of the input string.