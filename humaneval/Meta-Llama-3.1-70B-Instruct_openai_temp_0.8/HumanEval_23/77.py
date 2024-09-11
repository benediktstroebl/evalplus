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
    print("All test cases pass.")
```
This script defines a `strlen` function that calculates the length of a given string using Python's built-in `len` function. It includes a docstring that describes the function, its arguments, and its return value, and provides examples of how to use the function. The script also includes test cases to verify that the function behaves as expected.