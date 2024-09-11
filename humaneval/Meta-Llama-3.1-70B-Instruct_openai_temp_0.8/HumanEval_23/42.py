```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Test the function
if __name__ == "__main__":
    assert strlen('') == 0, "Test case 1 failed"
    assert strlen('abc') == 3, "Test case 2 failed"
    print("All test cases passed")
```

This Python script defines a function `strlen` that calculates the length of a given string using the built-in `len` function. The script includes a docstring for the function to describe its purpose, parameters, return value, and examples of usage. Additionally, it includes two test cases at the end to verify the correctness of the function.