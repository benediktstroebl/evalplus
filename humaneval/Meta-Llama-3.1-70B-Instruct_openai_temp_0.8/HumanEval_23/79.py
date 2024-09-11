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
    raise AssertionError("Test case 1 failed")
if strlen('abc')!= 3:
    raise AssertionError("Test case 2 failed")

print("All test cases passed")
```
In this script, the function `strlen` calculates the length of a given string using Python's built-in `len` function. The test cases at the end verify that the function behaves as expected. If all test cases pass, it prints "All test cases passed". If any test case fails, it raises an `AssertionError` with a corresponding message.