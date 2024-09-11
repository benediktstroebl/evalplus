### Palindrome Checker
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
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]
```
This script defines a function `is_palindrome` that checks whether a given string is a palindrome or not. It first removes any non-alphanumeric characters and converts the string to lowercase to make the comparison case-insensitive. Then it compares the cleaned text with its reverse using slicing (`text[::-1]`). If they are equal, the function returns `True`, indicating that the string is a palindrome; otherwise, it returns `False`.