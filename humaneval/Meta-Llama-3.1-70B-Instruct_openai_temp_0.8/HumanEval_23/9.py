```python
def strlen(string: str) -> int:
    """
    Return length of given string

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Example usage
if __name__ == "__main__":
    print(strlen(''))  # Output: 0
    print(strlen('abc'))  # Output: 3
```

This Python function `strlen` uses the built-in `len()` function to calculate and return the length of the given string. It handles the case of an empty string by returning 0. If you run this script, it will print the lengths of the example strings specified in the docstring, verifying the correctness of the `strlen` function.