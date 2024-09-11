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
    # Remove spaces and punctuation, and convert to lower case
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test the function
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```
This script defines a function `is_palindrome()` that takes a string as input, removes any non-alphanumeric characters, and converts the string to lower case. It then checks if the cleaned string is equal to its reverse. If they are equal, the function returns `True`, indicating that the original string is a palindrome. Otherwise, it returns `False`. The script includes example test cases to demonstrate the function's behavior.