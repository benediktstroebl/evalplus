```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    A string is a palindrome if it reads the same backward as forward.

    Args:
    text (str): The input string to be checked.

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
    text = text.lower()  # Convert to lowercase to handle case-insensitive comparison
    return text == text[::-1]  # Check if the string is equal to its reverse

# Test the function
print(is_palindrome(''))  # Expected output: True
print(is_palindrome('aba'))  # Expected output: True
print(is_palindrome('aaaaa'))  # Expected output: True
print(is_palindrome('zbcd'))  # Expected output: False
```

In this script, we define a function `is_palindrome` that takes a string as input and returns a boolean value indicating whether the string is a palindrome. We use the slicing syntax `text[::-1]` to reverse the string, and then check if the original string is equal to its reverse using the `==` operator. The function also converts the input string to lowercase to handle case-insensitive comparison. The script includes examples to demonstrate the function's behavior.