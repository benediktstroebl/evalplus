```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    Args:
    text (str): The input string.

    Returns:
    bool: True if the string is a palindrome, False otherwise.

    Examples:
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Remove leading and trailing whitespace, and convert to lowercase
    text = text.strip().lower()
    
    # Compare the original string with its reverse
    return text == text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(''))  # Expected: True
    print(is_palindrome('aba'))  # Expected: True
    print(is_palindrome('aaaaa'))  # Expected: True
    print(is_palindrome('zbcd'))  # Expected: False
```

This script provides a function `is_palindrome()` that checks if a given string is a palindrome. It removes leading and trailing whitespace, converts to lowercase, and then checks if the string is equal to its reverse. The `test cases` section at the end provides a basic example of how to use the function and demonstrates its expected behavior.