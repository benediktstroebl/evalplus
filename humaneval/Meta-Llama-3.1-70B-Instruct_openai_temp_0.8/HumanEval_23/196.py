```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Examples:
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
    print("All test cases pass")
```

This script defines a function `strlen` that takes a string as input and returns its length. It includes a docstring with documentation and examples, and test cases to verify the function's correctness. If all test cases pass, it prints "All test cases pass".