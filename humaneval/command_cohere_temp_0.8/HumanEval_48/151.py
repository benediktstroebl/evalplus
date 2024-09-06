Here's a Python function that checks if a given string is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    return text == text[::-1]
```
This function removes any non-alphanumeric characters and converts the text to lowercase to make the comparison case-insensitive. Then, it checks if the cleaned string is equal to its reverse, returning True if it is a palindrome and False otherwise. The docstring provides basic test cases that validate the functionality of the function.