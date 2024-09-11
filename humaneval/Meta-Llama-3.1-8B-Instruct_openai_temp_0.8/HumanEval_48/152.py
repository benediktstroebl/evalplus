### Palindrome Checker
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The string to be checked.

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
This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes non-alphanumeric characters and converts the string to lowercase to ensure the comparison is case-insensitive. Then it compares the cleaned string with its reverse. If they are the same, the function returns `True`, indicating that the string is a palindrome; otherwise, it returns `False`. The script also includes test cases to demonstrate the function's usage.