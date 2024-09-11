```markdown
### strlen Function

This Python script defines a function `strlen` that calculates the length of a given string.

```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The input string

    Returns:
        int: The length of the string

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)
```

### Example Usage

Here's an example of how to use the `strlen` function:

```python
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('hello world'))  # Output: 11
```

### Explanation

The `strlen` function uses the built-in `len` function in Python, which returns the number of items in an object. In this case, the object is a string, so `len` returns its length. The function takes a string as input, calculates its length using `len`, and returns the result as an integer.
```