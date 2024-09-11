```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    A string is a palindrome if it reads the same backward as forward.
    
    Args:
        text: The input string to check.
    
    Returns:
        True if the input string is a palindrome, False otherwise.
    """
    # Remove any leading or trailing whitespace and convert to lowercase
    text = text.strip().lower()
    # Compare the input string with its reverse
    return text == text[::-1]

# Example usage:
print(is_palindrome(""))  # True
print(is_palindrome("aba"))  # True
print(is_palindrome("aaaaa"))  # True
print(is_palindrome("zbcd"))  # False
```

In this script, the `is_palindrome` function uses Python's slicing feature to reverse the input string (`text[::-1]`), and then checks if the original string is equal to its reverse. This approach is case-insensitive and ignores leading/trailing whitespace.