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
assert strlen('') == 0, f"Test case assert strlen('') == 0 failed"
assert strlen('abc') == 3, f"Test case assert strlen('abc') == 3 failed"

print("All test cases passed.")
```

In this script, we define the `strlen` function that takes a string as an argument and returns its length using Python's built-in `len` function. We then include two test cases at the bottom of the script to ensure the function behaves as expected. If both test cases pass, it prints "All test cases passed."