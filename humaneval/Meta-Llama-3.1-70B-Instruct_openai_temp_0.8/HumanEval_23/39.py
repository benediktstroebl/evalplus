```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Example usage:
if __name__ == "__main__":
    print(strlen(''))  # Expected output: 0
    print(strlen('abc'))  # Expected output: 3
```

This script defines a function `strlen` that takes a string as an argument and returns its length using the built-in `len` function. The docstring includes usage examples as per the problem statement.

To run the script, save it in a file (e.g., `strlen.py`) and execute it using Python (e.g., `python strlen.py`). The script includes example usage in the `if __name__ == "__main__":` block, which will print the expected output when run directly.