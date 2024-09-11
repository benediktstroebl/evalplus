### Length of String
#### A Python Function to Calculate the Length of a Given String

```python
def strlen(string: str) -> int:
    """
    Return the length of the given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the string.

    Example:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)
```

You can run this script in your Python environment to test the function. It uses the built-in `len()` function to calculate the length of the string.

Note that this function does not perform any error checking. If you pass an argument that is not a string, it will raise a TypeError. If you want to add error checking, you can modify the function like this:

```python
def strlen(string: str) -> int:
    """
    Return the length of the given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the string.

    Example:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    return len(string)
```