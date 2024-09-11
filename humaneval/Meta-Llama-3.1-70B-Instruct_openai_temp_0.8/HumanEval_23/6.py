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
    assert strlen('') == 0, f"Expected strlen('') to return 0, but got {strlen('')}"
    assert strlen('abc') == 3, f"Expected strlen('abc') to return 3, but got {strlen('abc')}"
    print("All test cases pass.")
```

This script defines a function `strlen` that takes a string input and returns its length. The `if __name__ == "__main__":` block contains test cases that verify the function's correctness. When you run this script, it will either print "All test cases pass." if the function works correctly or raise an `AssertionError` with a descriptive message if any of the test cases fail.