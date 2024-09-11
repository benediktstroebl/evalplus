```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The input string to check

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
    # Remove spaces and convert to lowercase to handle case insensitivity and spaces
    cleaned_text = ''.join(text.split()).lower()
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
print(is_palindrome(''))  # Expected output: True
print(is_palindrome('aba'))  # Expected output: True
print(is_palindrome('aaaaa'))  # Expected output: True
print(is_palindrome('zbcd'))  # Expected output: False
```

In this script, we define the `is_palindrome` function that takes a string `text` as input, removes any spaces and converts it to lowercase, and checks if the resulting string is equal to its reverse (`cleaned_text[::-1]`). The function returns `True` if the string is a palindrome and `False` otherwise. We also include test cases at the end to demonstrate the function's behavior.