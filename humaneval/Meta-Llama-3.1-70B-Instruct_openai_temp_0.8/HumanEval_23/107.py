```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Example usage:
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

This script defines a function `strlen` that takes a string as input and returns its length. It uses the built-in `len` function in Python to calculate the length of the string.

You can run this script in your Python interpreter or save it as a Python file (e.g., `strlen.py`) and execute it using `python strlen.py`.