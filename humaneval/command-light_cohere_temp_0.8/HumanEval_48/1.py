Here is a Python script with a self-contained function that checks if a given string is a palindrome:
```python
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: string to check
    :return: boolean value of is palindrome
    """
    return text == text[::-1]
```

This script defines a function `is_palindrome` that takes a string `text` as input and returns a boolean value indicating whether the string is a palindrome. The function achieves this using the simplicity, comparing characters of the string with their reverse to check for the palindrome property.