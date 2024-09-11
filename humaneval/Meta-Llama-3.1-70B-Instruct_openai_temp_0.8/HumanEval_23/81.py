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
if strlen('')!= 0:
    raise AssertionError("Expected strlen('') to return 0")
if strlen('abc')!= 3:
    raise AssertionError("Expected strlen('abc') to return 3")

print("All test cases passed.")
```