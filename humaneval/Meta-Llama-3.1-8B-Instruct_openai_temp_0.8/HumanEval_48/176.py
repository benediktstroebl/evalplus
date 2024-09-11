```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the input string is a palindrome, False otherwise.

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
    # Remove spaces and punctuation, and convert to lowercase
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]

# Test the function
print(is_palindrome(''))  # Expected output: True
print(is_palindrome('aba'))  # Expected output: True
print(is_palindrome('aaaaa'))  # Expected output: True
print(is_palindrome('zbcd'))  # Expected output: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes spaces and punctuation from the string and converts it to lowercase, then checks if the cleaned string is the same when reversed. The function returns `True` if the string is a palindrome and `False` otherwise. The script then tests the function with the provided examples.