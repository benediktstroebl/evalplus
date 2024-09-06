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
    # Convert string to list to allow indexing from both sides
    text = text.split('')
    # Check if the reversed list is equal to the original list
    return text == text[::-1]
```
This function utilizes string slicing (`text[::-1]`) to reverse the string and then checks if the original string is equal to its reverse, indicating if it's a palindrome. The empty string is considered valid input, returning True, while non-empty inverted strings are correctly identified as palindromes.