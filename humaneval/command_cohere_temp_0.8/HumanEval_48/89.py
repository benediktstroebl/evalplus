```python
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase to handle case-sensitive palindrome check
    return text.lower() == text[::-1].lower()
```
This function uses string slicing and concatenation to reverse the string and then compares it to the original string. The `lower()` method is used to convert both strings to lowercase to make the comparison case-insensitive. This approach eliminates the need for a reverse function and provides a concise solution.