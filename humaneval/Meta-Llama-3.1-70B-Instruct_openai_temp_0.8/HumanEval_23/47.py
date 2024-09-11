```python
def strlen(string: str) -> int:
    """
    Return length of given string

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Example usage:
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```
This Python script defines a function `strlen` that calculates the length of a given string using the built-in `len` function. The docstring includes doctests to verify the function's behavior. The example usage at the end demonstrates how to call the function with different inputs.