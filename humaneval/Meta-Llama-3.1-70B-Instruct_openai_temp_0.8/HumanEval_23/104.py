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

# Test cases
assert strlen('') == 0
assert strlen('abc') == 3
print("All test cases pass.")
```

To run this script, save it as a.py file and run it using Python. The `assert` statements at the end will check the function against the test cases and print "All test cases pass." if they all pass, or raise an `AssertionError` if any of them fail.