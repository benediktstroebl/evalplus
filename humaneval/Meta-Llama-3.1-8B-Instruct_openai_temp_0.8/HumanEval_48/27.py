```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
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
```

This script defines the `is_palindrome` function to check if a given string is a palindrome. It first removes any spaces and converts the string to lowercase for case-insensitive comparison. Then, it checks if the string is equal to its reverse. If they are equal, the function returns `True`; otherwise, it returns `False`. The script also includes test cases to verify the correctness of the function.