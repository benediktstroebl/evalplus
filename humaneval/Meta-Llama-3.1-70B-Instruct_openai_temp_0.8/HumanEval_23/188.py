```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


# Example use cases
if __name__ == "__main__":
    print(strlen(''))  # Expected output: 0
    print(strlen('abc'))  # Expected output: 3
    print(strlen('Hello, World!'))  # Expected output: 13
```

In this script, we define a function called `strlen` that takes a string as input and returns the length of that string. The function simply calls Python's built-in `len` function to calculate the length.

The `if __name__ == "__main__":` block includes example use cases. When the script is run directly, it will print the length of the given strings.