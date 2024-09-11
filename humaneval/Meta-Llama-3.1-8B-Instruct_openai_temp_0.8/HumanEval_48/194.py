```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string.

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
```

In this solution, we first remove all non-alphanumeric characters from the input string using a generator expression. Then, we convert the resulting string to lowercase to make the palindrome check case-insensitive. Finally, we compare the cleaned string with its reverse (`[::-1]` is a Python slice that steps backwards through the entire string). If they are equal, then the original string is a palindrome.