```python
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: boolean
    """
    # Convert string to list to allow reversed() to work
    text = list(text)
    return text == text[::-1]
```