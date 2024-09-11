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

# Test the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
print(strlen('Hello, World!'))  # Expected output: 13
```

This script defines a function `strlen` that takes a string as input and returns its length using the built-in Python function `len`. The function is then tested with a few examples to verify its correctness.

However, if you want to implement this function manually, you can do it by iterating over the characters in the string:

```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    length = 0
    for _ in string:
        length += 1
    return length

# Test the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
print(strlen('Hello, World!'))  # Expected output: 13
```

Or using recursion:

```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if not string:
        return 0
    else:
        return 1 + strlen(string[1:])

# Test the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
print(strlen('Hello, World!'))  # Expected output: 13
```