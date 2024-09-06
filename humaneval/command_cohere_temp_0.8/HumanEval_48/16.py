```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    text = text.lower()  # Convert to lowercase for case-insensitive comparison
    return text == text[::-1]
```
This function first converts the input text to lowercase to ensure that the comparison is case-insensitive. It then uses the slice operator [::-1] to reverse the string and compares it with the original text to determine if it's a palindrome.