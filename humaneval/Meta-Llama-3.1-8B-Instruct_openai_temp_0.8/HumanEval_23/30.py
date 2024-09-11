### strlen Function
#### Returns the length of a given string

```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): Input string

    Returns:
        int: Length of the input string

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)
```

You can save this script to a file and run it in your Python environment. The `len()` function is a built-in Python function that returns the number of items in an object. In the case of a string, it returns the number of characters in the string. 

Alternatively, if you want to implement the `strlen` function manually without using the `len()` function, you can use a loop to count the characters:

```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): Input string

    Returns:
        int: Length of the input string

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    length = 0
    for char in string:
        length += 1
    return length
```

This version of the `strlen` function will have a time complexity of O(n), where n is the length of the string, because it needs to iterate over each character in the string to count them.