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
This function first removes any non-alphanumeric characters and converts the text to lowercase to make the comparison case-insensitive. It then computes the reversed version of the cleaned text and checks if it's the same as the original text, thereby determining if it's a palindrome. 

This approach ensures that punctuations, spaces, and capitalization won't influence the result, and the function can effectively determine whether the input text is a palindrome as per the specified tests.