Here's a self-contained Python script that defines a function `strlen` that computes the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns 0 if string is empty"""
    return len(string) if string else 0
```

This code defines a function `strlen` that calculates the length of a given string. It returns 0 if the  and returns the length of the string using the `len()` function if the input is not empty.