### Palindrome Checker
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    A palindrome is a string that reads the same backward as forward.

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

# Test cases
print(is_palindrome(''))  # Expected: True
print(is_palindrome('aba'))  # Expected: True
print(is_palindrome('aaaaa'))  # Expected: True
print(is_palindrome('zbcd'))  # Expected: False
```
In this script, the `is_palindrome` function takes a string as input, removes any non-alphanumeric characters, converts the string to lowercase, and then checks if the cleaned string is the same when reversed. If it is, the function returns `True`; otherwise, it returns `False`.