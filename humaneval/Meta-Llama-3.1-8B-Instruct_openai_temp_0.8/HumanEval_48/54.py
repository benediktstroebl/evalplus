```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove any leading or trailing whitespace
    text = text.strip()
    
    # Convert the string to lowercase to make the comparison case-insensitive
    text = text.lower()
    
    # Compare the string with its reverse
    return text == text[::-1]


# Example usage:
print(is_palindrome(""))  # True
print(is_palindrome("aba"))  # True
print(is_palindrome("aaaaa"))  # True
print(is_palindrome("zbcd"))  # False
```

In this script, the `is_palindrome` function first removes any leading or trailing whitespace from the input string using the `strip` method. Then, it converts the string to lowercase using the `lower` method to make the comparison case-insensitive.

Finally, it compares the string with its reverse using slicing (`text[::-1]`). If the string is equal to its reverse, it returns `True`; otherwise, it returns `False`.