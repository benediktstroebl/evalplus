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
    return text == text[::-1]
```
This function removes any non-alphanumeric characters and converts the text to lowercase to make the comparison case-insensitive. Then, it checks if the cleaned text is the same as its reversed version to determine if it's a palindrome. The function includes type hints to indicate the expected input and return type, which improves code readability and helps with introspection and debugging. Additionally, the docstring provides a clear explanation of the function's purpose and behavior, making the code more understandable and maintainable.