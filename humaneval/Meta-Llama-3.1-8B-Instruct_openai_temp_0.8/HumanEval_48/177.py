```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check.

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
    # Remove spaces and convert to lowercase
    text = text.replace(' ', '').lower()
    
    # Compare the string with its reverse
    return text == text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(''))  # True
    print(is_palindrome('aba'))  # True
    print(is_palindrome('aaaaa'))  # True
    print(is_palindrome('zbcd'))  # False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes any spaces from the string and converts it to lowercase. Then it compares the string with its reverse using slicing (`text[::-1]`). If they are the same, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`. The script includes test cases at the end to demonstrate the function's behavior.