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
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All test cases pass")
```

However, here's a more pythonic version of the same function without using built-in function `len()`:

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
    for _ in string:
        count += 1
    return count

# Test cases
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All test cases pass")
```

Or using recursion:

```python
def strlen(string: str) -> int:
    """
    Return length of given string

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if string == '':
        return 0
    else:
        return 1 + strlen(string[1:])

# Test cases
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All test cases pass")
```