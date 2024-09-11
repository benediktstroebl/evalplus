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
    assert strlen('') == 0, f"Expected strlen('') to return 0, but got {strlen('')}"
    assert strlen('abc') == 3, f"Expected strlen('abc') to return 3, but got {strlen('abc')}"
    print("All test cases pass")
```

This script defines a function `strlen` that takes a string as input and returns its length. The `len` function is a built-in Python function that returns the number of items in an object. 

In the test cases, we use the `assert` statement to check if the output of the `strlen` function matches the expected output. If the output does not match, an `AssertionError` is raised. If all test cases pass, it prints "All test cases pass".