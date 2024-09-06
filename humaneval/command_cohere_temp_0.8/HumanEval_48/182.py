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
    
    # Check if text is same when reading forward and backward
    return text == text[::-1]
```
This function first cleans the input by converting it to lowercase and removing all non-alphanumeric characters using a list comprehension. Then, it performs the palindrome check by comparing the cleaned string with its reverse using slicing. The function returns True if the string is a palindrome and False otherwise.