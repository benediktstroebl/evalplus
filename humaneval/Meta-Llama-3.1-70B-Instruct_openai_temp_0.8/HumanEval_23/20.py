```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

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
    print("All test cases passed.")
```

This script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function. The function includes a docstring that describes its behavior, parameters, return value, and provides examples.

The script also includes test cases to verify the correctness of the `strlen` function. The `assert` statements check if the function returns the expected results for different inputs. If all test cases pass, the script prints "All test cases passed."