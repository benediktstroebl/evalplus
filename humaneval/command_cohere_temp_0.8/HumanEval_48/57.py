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
    
    # Check if the reversed text matches the original text
    return text == text[::-1]
```
This function removes any non-alphanumeric characters and converts the text to lowercase to handle cases like 'Aba' versus 'aba' and 'AAAB' versus 'aaAAbb'. Then it compares the original text with its reverse to determine if it's a palindrome. The 'text[::-1]' slicing expression generates a reversed copy of the text.