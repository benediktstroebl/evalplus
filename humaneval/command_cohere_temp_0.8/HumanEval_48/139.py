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
    # Convert string to list to allow reversed iteration
    text = list(text)
    # Compare each character in the string with its reverse
    return text == text[::-1]
```

This function leverages Python's powerful list comprehension to reverse the string and then compare it to the original text character by character, ensuring an efficient and concise check for palindromes.