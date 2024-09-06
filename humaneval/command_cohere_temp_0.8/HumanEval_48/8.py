Here's a Python function that checks if a given text is a palindrome:
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
    # Test Case 1
    assert is_palindrome('') == True
    # Test Case 2
    assert is_palindrome('aba') == True
    # Test Case 3
    assert is_palindrome('aaaaa') == True
    # Test Case 4
    assert is_palindrome('zbcd') == False
```
The function uses a couple of tricks to make the palindrome checking process more efficient:
1. removes non-alphanumeric characters, which ensures that the string consists only of letters and digits.
2. converts the string to lowercase, which ensures that the palindrome check is case-insensitive. 

Then, it uses string slicing to reverse the string and checks if it's the same as the original text.