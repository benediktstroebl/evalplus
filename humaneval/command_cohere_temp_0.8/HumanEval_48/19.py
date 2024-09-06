```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to list to allow indexing from both sides
    text = list(text)
    # Check if text is equal to its reversed version
    return text == text[::-1]
```

This function uses list manipulation to check if a string is equal to its reversed version, which is the defining characteristic of a palindrome. The function passes the provided tests:
```python
>>> is_palindrome('')
True
>>> is_palindrome('aba')
True
>>> is_palindrome('aaaaa')
True
>>> is_palindrome('zbcd')
False
```