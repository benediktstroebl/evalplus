### strlen Function Implementation

Here is a simple Python function to return the length of a given string:

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

### Explanation

This function uses the built-in `len()` function in Python, which returns the number of items in an object, such as the number of characters in a string. 

### Usage

To use this function, simply call it with a string argument and it will return the length of the string.

```python
print(strlen('hello'))  # Output: 5
print(strlen('world'))  # Output: 5
print(strlen(''))       # Output: 0
```