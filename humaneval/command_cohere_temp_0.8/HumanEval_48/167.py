Here's a Python function that checks if a given text is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: boolean -- True if it is a palindrome, False otherwise
    """
    # Convert text to lowercase to handle case-insensitive palindromes
    text = text.lower()
    # Check if text is an empty string
    if not text:
        return True
    # Check if text is a palindrome by comparing characters from beginning and end
    return text[0:] == text[::-1]
```
This function passes the provided tests:
```
def test_is_palindrome():
    # Basic tests
    assert is_palindrome('')
    assert is_palindrome('aba')
    assert is_palindrome('aaaaa')

    # Case-insensitive palindromes
    assert is_palindrome('OOoo')

    # Non-palindrome
    assert not is_palindrome('zbcd')
```
The function first converts the text to lowercase to handle case-insensitive palindromes. If the text is empty, it is considered a palindrome. The function then compares characters from the beginning and end of the text to check if it's a palindrome, returning `True` if they match and `False` otherwise.