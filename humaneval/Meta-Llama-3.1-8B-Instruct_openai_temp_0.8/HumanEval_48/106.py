```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): Input string

    Returns:
        bool: True if string is a palindrome, False otherwise

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
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


if __name__ == "__main__":
    # Test the function
    print(is_palindrome(""))  # Expected output: True
    print(is_palindrome("aba"))  # Expected output: True
    print(is_palindrome("aaaaa"))  # Expected output: True
    print(is_palindrome("zbcd"))  # Expected output: False
```

This Python script includes a function `is_palindrome()` that checks if a given string is a palindrome. The function first removes non-alphanumeric characters and converts the string to lowercase to make it case-insensitive. It then compares the cleaned string with its reverse. If they are the same, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`.