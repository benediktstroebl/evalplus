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
    
    # Check if the reversed string matches the original string
    return text == text[::-1]
```
This function leverages string manipulation and the slice notation ([::-1]) to check if a given string is a palindrome. The slice notation reverses the string, and the rebuilt string is then compared to the reversed version to determine if it's a palindrome. The function passes the provided tests: `` is_palindrome('') `` returns True, `` is_palindrome('aba') `` returns True, and `` is_palindrome('zbcd') `` returns False.  Additionally, the function is designed to be case-insensitive and handles non-alphanumeric characters by removing them prior to analysis.