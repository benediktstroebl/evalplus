```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)


import doctest

if __name__ == "__main__":
    doctest.testmod()
```

This script defines a function `strlen` that calculates the length of a given string. The function is documented with a docstring that includes examples of usage, which can be verified using the `doctest` module. 

You can run this script, and `doctest` will automatically check that the examples in the docstring produce the expected output. If all examples pass, there will be no output. If any examples fail, you will see an error message indicating the failure.