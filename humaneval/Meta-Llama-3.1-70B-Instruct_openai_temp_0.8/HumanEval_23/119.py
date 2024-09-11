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

# Test cases
if __name__ == "__main__":
    assert strlen('') == 0, f"Expected strlen('') to return 0, but got {strlen('')}"
    assert strlen('abc') == 3, f"Expected strlen('abc') to return 3, but got {strlen('abc')}"
    print("All test cases pass")
```