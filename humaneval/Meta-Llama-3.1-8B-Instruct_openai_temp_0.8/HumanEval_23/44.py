```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The input string

    Returns:
        int: The length of the string

    Example:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)


# Test the function
if __name__ == "__main__":
    print(strlen(""))  # Output: 0
    print(strlen("abc"))  # Output: 3
```