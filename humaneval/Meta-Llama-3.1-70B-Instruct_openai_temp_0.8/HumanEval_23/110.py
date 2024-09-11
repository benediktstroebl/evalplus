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


# Example usage
if __name__ == "__main__":
    # Test cases
    print(strlen(''))  # Expected output: 0
    print(strlen('abc'))  # Expected output: 3
    print(strlen('Hello, World!'))  # Expected output: 13

    # Additional test case with non-English characters
    print(strlen('नमस्ते'))  # Expected output: 6
```