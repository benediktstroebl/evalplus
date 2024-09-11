```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    A palindrome is a string that reads the same backward as forward.
    
    Args:
    text (str): Input string to check.

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


# Example usage:
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```

In this script, we define a function `is_palindrome` that takes a string `text` as an argument. The function first removes any non-alphanumeric characters from the string and converts it to lowercase to ensure the palindrome check is case-insensitive. It then checks if the cleaned text is equal to its reverse (`text[::-1]` is a Python idiom to get the characters of a string in reverse order). If the two are equal, the function returns `True`, indicating that the original string is a palindrome. Otherwise, it returns `False`.