```python
def strlen(string: str) -> int:
    """
    Return the length of the given string.

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
This script defines the `strlen` function as specified and includes example usage in the `if __name__ == "__main__":` block. The `len` function in Python returns the number of items in an object, in this case, the number of characters in a string.