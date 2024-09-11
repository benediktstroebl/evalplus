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
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()

    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test the function
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
print(is_palindrome('A man, a plan, a canal: Panama'))  # True
print(is_palindrome('Not a palindrome'))  # False
```

In this script, the `is_palindrome` function removes all non-alphanumeric characters from the input string and converts it to lowercase. It then checks if the cleaned string is the same when its characters are reversed. If they are the same, the function returns `True`; otherwise, it returns `False`. The script also includes test cases to demonstrate the function's usage.