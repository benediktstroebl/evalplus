Here is a self-contained Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Testing the function
>>> strlen('')
0

>>> strlen('abc')
3

>>> strlen('')abc')
3
```

This code defines a function `strlen` that takes a string as input and returns its length. The function uses the string's `len` function to get its length.