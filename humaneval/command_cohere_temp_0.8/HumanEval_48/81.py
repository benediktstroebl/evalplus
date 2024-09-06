Here's a Python function that checks if a given text is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if text is same when reading forward and backward
    return text == text[::-1]
```
This function first removes all non-alphanumeric characters and converts the text to lowercase to make the comparison case-insensitive and to ignore punctuation, whitespace, and other non-alphanumeric characters. Then, it compares the cleaned string with its reverse using slicing (`s[::-1]`) to efficiently reverse the string. The function returns `True` if the cleaned string is the same as its reverse, indicating it is a palindrome, and `False` otherwise.