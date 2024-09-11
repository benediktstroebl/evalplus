```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Example usage:
if __name__ == "__main__":
    print(strlen(""))  # Output: 0
    print(strlen("abc"))  # Output: 3
```

This script defines a function `strlen` that calculates the length of a given string. It utilizes Python's built-in `len` function to achieve this. The `if __name__ == "__main__":` block serves as an entry point for the script, allowing users to test the function directly when they run the script.