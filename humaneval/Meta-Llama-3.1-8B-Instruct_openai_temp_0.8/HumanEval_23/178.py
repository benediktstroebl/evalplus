```markdown
### strlen Function

The following Python script defines a function `strlen` that calculates the length of a given string.

```python
def strlen(string: str) -> int:
    """
    Return length of given string

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
```

### Explanation

*   The `strlen` function takes a string as input and returns its length.
*   It uses the built-in `len` function in Python, which returns the number of items in an object.
*   The function includes a docstring that provides a description, specifies the input parameter, and lists examples of usage.

### Usage

You can use the `strlen` function like this:

```python
print(strlen('Hello, World!'))  # Output: 13
print(strlen(''))  # Output: 0
print(strlen('Python'))  # Output: 6
```

This script is a simple, self-contained solution that defines a reusable function for calculating string lengths.