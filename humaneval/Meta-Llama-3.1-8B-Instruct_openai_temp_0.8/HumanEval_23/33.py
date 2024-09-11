```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Example usage:
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
print(strlen("hello world"))  # Output: 11
```

In this script, we define a function `strlen` that takes a string as input and returns its length using the built-in `len` function. The docstring provides documentation for the function and includes examples of usage. The example usage section demonstrates how to call the `strlen` function with different inputs and print the results.