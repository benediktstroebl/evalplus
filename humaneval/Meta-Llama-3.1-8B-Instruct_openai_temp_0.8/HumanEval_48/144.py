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
    # Remove spaces and convert to lowercase to make the comparison case-insensitive
    text = ''.join(text.split()).lower()
    # Compare the input string with its reverse
    return text == text[::-1]


# Example usage:
if __name__ == "__main__":
    print(is_palindrome(""))  # True
    print(is_palindrome("aba"))  # True
    print(is_palindrome("aaaaa"))  # True
    print(is_palindrome("zbcd"))  # False
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("Not a palindrome"))  # False
```

This Python script defines a function `is_palindrome` that checks if a given string is a palindrome. The function removes spaces and converts the input to lowercase to make the comparison case-insensitive. It then compares the input string with its reverse. If they are equal, the function returns `True`; otherwise, it returns `False`. The examples demonstrate the usage of the function.