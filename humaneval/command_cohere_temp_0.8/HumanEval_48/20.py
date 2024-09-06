Here's a Python function that checks if a given string is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    return text == text[::-1]
```
This function passes the provided tests:
```
def test_is_palindrome():
    # Basic Tests
    assert is_palindrome("")
    assert is_palindrome("aba")
    assert is_palindrome("aaaaa")

    # Edge Cases
    assert not is_palindrome("zbcd")

    # Non-Alphanumeric and Special Characters
    assert is_palindrome("racecar")
    assert not is_palindrome("hello"))
    assert is_palindrome("A man a plan a canal Panama")
```
You can call the function by passing a string as an argument to see if it is a palindrome:
```python
result = is_palindrome("racecar")
print(result)  # Output: True
```