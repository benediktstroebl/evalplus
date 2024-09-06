Here's a Python function that checks if a given text is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert text to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    return text == text[::-1]
```
This function passes the provided tests:
```
def test_palindrome():
    # Test String with Non-Alphanumeric Characters
    assert is_palindrome('aba') == True
    assert is_palindrome('aaaaa') == True
    assert is_palindrome('Hello World!') == False

    # Test Empty String
    assert is_palindrome('') == True

    # Test String with Mix of Uppercase and Lowercase
    assert is_palindrome('A man a plan a canal Panama') == True

    # Test with Numbers Only
    assert is_palindrome('12321') == True

    # Test with Mix of Alphanumeric and Non-Alphanumeric Characters
    assert is_palindrome('race car') == True
    assert is_palindrome('zbcd') == False
```
**Explanation:**
1. The function `is_palindrome` takes a string text as an argument and returns a boolean value (`True` if it's a palindrome, `False` otherwise).
2. It first converts the input text to lowercase using the `.lower()` method and removes any non-alphanumeric characters using a list comprehension `(c for c in text if c.isalnum())`.
3. Then, it checks if the cleaned string is equal to its reverse using slicing `text[::-1]`. The slicing notation `[::-1]` creates a reversed copy of the string.
4. If the original and reversed strings are the same, the function returns `True`; otherwise, it returns `False`.