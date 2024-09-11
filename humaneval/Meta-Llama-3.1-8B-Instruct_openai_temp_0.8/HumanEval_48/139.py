```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    A palindrome is a string that reads the same backwards as forwards.

    Args:
        text (str): The string to check.

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
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test the function
print(is_palindrome(""))  # True
print(is_palindrome("aba"))  # True
print(is_palindrome("aaaaa"))  # True
print(is_palindrome("zbcd"))  # False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes non-alphanumeric characters and converts the string to lowercase, then compares the cleaned string with its reverse. The function returns `True` if the string is a palindrome and `False` otherwise. The script includes example use cases to demonstrate the function's behavior.