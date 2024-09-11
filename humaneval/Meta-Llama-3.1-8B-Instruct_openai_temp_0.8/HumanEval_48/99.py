```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The input string to check

    Returns:
    bool: True if the string is a palindrome, False otherwise

    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Remove any whitespace and convert to lowercase
    cleaned_text = ''.join(c for c in text if c.isalnum()).lower()
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example usage:
print(is_palindrome(""))  # Expected output: True
print(is_palindrome("aba"))  # Expected output: True
print(is_palindrome("aaaaa"))  # Expected output: True
print(is_palindrome("zbcd"))  # Expected output: False
```

This script uses Python's built-in slicing functionality (`[::-1]`) to reverse the cleaned text. It also uses a generator expression to remove any non-alphanumeric characters from the input text, and the `isalnum()` method to check if a character is alphanumeric. The `lower()` method is used to ensure the comparison is case-insensitive.