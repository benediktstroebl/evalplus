```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The string to check

    Returns:
    bool: True if the string is a palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase for case-insensitive comparison
    text = text.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return text == text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(""))  # Expected output: True
    print(is_palindrome("aba"))  # Expected output: True
    print(is_palindrome("aaaaa"))  # Expected output: True
    print(is_palindrome("zbcd"))  # Expected output: False
    print(is_palindrome("radar"))  # Expected output: True
    print(is_palindrome("hello"))  # Expected output: False
```

This script defines the `is_palindrome` function, which checks if a given string is a palindrome by removing spaces, converting to lowercase, and comparing the string with its reverse. The `test cases` section demonstrates the function's usage with various inputs.