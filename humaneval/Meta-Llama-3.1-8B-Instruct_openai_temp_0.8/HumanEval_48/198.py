```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The input string to check

    Returns:
    bool: True if the string is a palindrome, False otherwise

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
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]

# Test cases
print(is_palindrome(""))  # Expected output: True
print(is_palindrome("aba"))  # Expected output: True
print(is_palindrome("aaaaa"))  # Expected output: True
print(is_palindrome("zbcd"))  # Expected output: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. The function first removes any non-alphanumeric characters and converts the text to lowercase to ensure the comparison is case-insensitive. It then compares the cleaned text with its reverse using slicing (`[::-1]`). If the two strings are equal, the function returns `True`, indicating that the input string is a palindrome. Otherwise, it returns `False`. The script includes test cases to demonstrate the function's behavior.