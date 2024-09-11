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
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All test cases passed")
```

This script defines the `strlen` function, which uses Python's built-in `len` function to calculate the length of a given string. It also includes test cases to verify the function's correctness.

You can run the script to check if all test cases pass. If the function is implemented correctly, it will print "All test cases passed".