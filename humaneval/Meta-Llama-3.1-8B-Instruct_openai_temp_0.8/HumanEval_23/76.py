### len() Function in Python

Python has a built-in `len()` function that returns the number of items in an object. So, you don't need a separate function to get the length of a string.

However, for the sake of the problem, here's a Python script with the `strlen` function implemented:

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

# Test cases
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```

Alternatively, if you want to implement it manually without using the `len()` function, here's a version using a for loop:

```python
def strlen(string: str) -> int:
    """
    Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    count = 0
    for char in string:
        count += 1
    return count

# Test cases
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```