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
    assert strlen('') == 0, "Test case 1 failed"
    assert strlen('abc') == 3, "Test case 2 failed"
    assert strlen('hello world') == 11, "Test case 3 failed"
    print("All test cases passed")
```