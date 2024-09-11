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
assert strlen('') == 0
assert strlen('abc') == 3
print("All test cases pass")
```

You can copy and paste this script into a Python interpreter or save it to a file and run it to verify its correctness. The test cases at the end ensure that the function behaves as expected.