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

# Test cases
if __name__ == "__main__":
    assert strlen('') == 0, "Test case '' failed"
    assert strlen('abc') == 3, "Test case 'abc' failed"
    print("All test cases passed")
```