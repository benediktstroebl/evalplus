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
    
    # Check if text is same when read forward and backward
    return text == text[::-1]
```
This function first removes all non-alphanumeric characters and converts the text to lowercase to make the comparison case-insensitive. It then uses slicing to reverse the text and checks if it's the same as the original text. The function returns True if it's a palindrome and False otherwise.

Here is how you can use this function:
```python
# This test suite runs the function checks for the palindrome property.
assert is_palindrome("")
assert is_palindrome("aba")
assert is_palindrome("aaaaa")
assert not is_palindrome("zbcd")
```
This function will yield the expected results based on the provided test cases.