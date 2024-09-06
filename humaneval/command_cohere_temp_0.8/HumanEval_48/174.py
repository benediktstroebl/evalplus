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
This function first removes any non-alphanumeric characters and converts the text to lowercase to make the comparison case-insensitive. It then compares the original text with its reversed version to determine if it's a palindrome. The function returns True if it is, and False otherwise. 

This approach ensures that the function can successfully determine whether any given input is a palindrome, as demonstrated in the provided test cases.