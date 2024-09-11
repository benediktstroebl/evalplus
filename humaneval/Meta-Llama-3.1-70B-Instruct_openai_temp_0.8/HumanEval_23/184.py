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
print(strlen('') == 0)  # Expected output: True
print(strlen('abc') == 3)  # Expected output: True

# If no AssertionError is thrown, all test cases pass
try:
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All test cases pass")
except AssertionError:
    print("Test cases failed")
```

To run the tests, save the code in a file (e.g., `strlen.py`) and run it with Python (e.g., `python strlen.py`). If all test cases pass, it will print "All test cases pass." If any test case fails, it will print "Test cases failed."