```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test cases
if __name__ == "__main__":
    assert strlen('') == 0, "Test case failed: Empty string length should be 0"
    assert strlen('abc') == 3, "Test case failed: 'abc' string length should be 3"
    print("All test cases pass")
```