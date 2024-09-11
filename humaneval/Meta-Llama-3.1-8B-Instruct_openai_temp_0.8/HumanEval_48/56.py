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
    # Remove spaces and convert to lower case for case-insensitive comparison
    text = text.replace(' ', '').lower()
    
    # Compare the string with its reverse
    return text == text[::-1]


# Example usage
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
print(is_palindrome('Able was I ere I saw Elba'))  # True
print(is_palindrome('Hello'))  # False
```
This Python script defines a function named `is_palindrome` that checks whether a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). The script includes example usage cases at the end to demonstrate the function's behavior.