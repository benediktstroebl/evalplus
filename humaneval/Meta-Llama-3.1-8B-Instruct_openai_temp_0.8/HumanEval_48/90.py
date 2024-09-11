### Palindrome Checker
#### Python Script

```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.
    
    Args:
    text (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    
    # Remove any spaces and convert to lowercase for case insensitive comparison
    text = text.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return text == text[::-1]

# Example usage:
print(is_palindrome(""))  # True
print(is_palindrome("aba"))  # True
print(is_palindrome("aaaaa"))  # True
print(is_palindrome("zbcd"))  # False
```

This script uses Python's slicing feature (`text[::-1]`) to reverse the input string, and then compares it with the original string. If they are the same, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`. The function also removes any spaces from the input string and converts it to lowercase to make the comparison case-insensitive.