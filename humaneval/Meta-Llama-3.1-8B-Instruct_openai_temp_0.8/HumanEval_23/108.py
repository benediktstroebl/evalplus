Here's a simple Python script that defines a function `strlen` to calculate the length of a given string:

```markdown
# strlen Function
================

### Description
This function returns the length of a given string.

### Code
```python
def strlen(string: str) -> int:
    """
    Return length of given string.

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

### Usage
To use this function, you can call it with a string argument and print the result. Here's an example:

```python
print(strlen('hello'))  # Output: 5
print(strlen('world'))  # Output: 5
```

### Note
The `len()` function in Python is used to get the length of a sequence (such as a string, list, or tuple). This `strlen` function simply wraps the `len()` function for clarity and readability.