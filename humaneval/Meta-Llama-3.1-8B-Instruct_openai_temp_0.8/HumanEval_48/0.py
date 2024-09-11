### Palindrome Checker
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

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
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]

# Example usage:
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```
This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes any non-alphanumeric characters from the string and converts it to lowercase, and then compares the cleaned string with its reverse. If they are the same, the function returns `True`; otherwise, it returns `False`. The script also includes example usage at the end to demonstrate how to use the function.