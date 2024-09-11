```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    
    Args:
    text (str): The input string
    
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
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test the function
print(is_palindrome(''))  # Expected output: True
print(is_palindrome('aba'))  # Expected output: True
print(is_palindrome('aaaaa'))  # Expected output: True
print(is_palindrome('zbcd'))  # Expected output: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes all non-alphanumeric characters and converts the string to lowercase to ensure the comparison is case-insensitive and ignores punctuation. Then it compares the cleaned string with its reverse. If they are equal, the function returns `True`; otherwise, it returns `False`. The script also includes test cases to verify the function's correctness.