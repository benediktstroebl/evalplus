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

# Test the function
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All tests passed.")
```