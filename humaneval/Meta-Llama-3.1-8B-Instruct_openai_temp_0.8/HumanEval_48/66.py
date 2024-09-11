```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The input string to be checked

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
    # Remove all spaces and convert to lowercase for case-insensitive comparison
    cleaned_text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]

# Test the function
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes all non-alphanumeric characters and converts the string to lowercase to make the comparison case-insensitive. Then it compares the cleaned string with its reverse. If they are the same, the function returns True, indicating that the string is a palindrome. Otherwise, it returns False. The script also includes test cases to demonstrate its functionality.