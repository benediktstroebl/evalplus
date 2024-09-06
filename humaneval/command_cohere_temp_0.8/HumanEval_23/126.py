```python
def strlen(s: str) -> int:
    """Returns the length of a string."""
    return len(s)
```

This Python script defines a function called `strlen` that takes a string as an argument and returns the length of that string. The function uses the `len()` function, which is a built-in Python function, to determine the number of characters in the string. 

This behaves as intended, returning 0 for an empty string, and 3 for the string 'abc':
```python
>>> strlen('')
0
>>> strlen('abc')
3
```

This provides a practical and efficient way to determine the length of a string in Python.