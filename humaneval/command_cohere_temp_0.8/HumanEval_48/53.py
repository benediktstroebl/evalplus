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
    
    # Check if text is same when reversed
    return text == text[::-1]
```
This function removes any non-alphanumeric characters and converts the text to lowercase to make the comparison case-insensitive. Then, it compares the original text with its reverse using slicing to determine if it's a palindrome. The function returns True for palindromes and False otherwise, as the problem statement requires.