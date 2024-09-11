### Length of a String in Python

Here's a self-contained Python script that solves the problem using a function called `strlen`:

```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Test the function
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```

In this script, we define a function `strlen` that takes a string as input and returns its length using the built-in `len` function in Python. We then test the function with two examples.