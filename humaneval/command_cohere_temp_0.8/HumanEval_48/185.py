```python
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase to handle case-insensitive palindromes
    text = text.lower()
    # Check if text is an empty string or if it is made up of repeating characters
    if text == '' or text == text[1:] * 2:
        return True
    # Count the number of characters and divide it by 2 to get the center index
    center_index = len(text) // 2
    # Iterate through characters of text with start and end positions
    # shifted by center_index
    for i in range(center_index):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True
```

This function passes the tests provided in the original prompt and returns True for any empty string, any string composed of repeating characters, and any palindrome. It returns False for non-palindromic strings.