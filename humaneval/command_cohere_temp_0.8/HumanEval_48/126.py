Here's a Python function that checks if a given text is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: boolean -- True if it is a palindrome, False otherwise
    """
    # Convert string to lowercase to handle case-insensitive palindromes
    text = text.lower()
    # Check if text is an empty string
    if not text:
        return True
    # Check if text is a palindrome by comparing characters from beginning and end
    return text[0] == text[-1] and is_palindrome(text[1:-1])
```
This function uses a recursive approach to solve the problem. It first checks if the given text is empty, returning True if so as an empty string is a palindrome. It then checks the first character of the text with the last character of the text to see if they are the same. Finally, the function recursively checks if the rest of the string, excluding the first and last characters, is a palindrome. The string is a palindrome if the first and last characters are the same and the rest of the string is also a palindrome. The function returns False if the text is not a palindrome. 

To follow best practices, the function includes type hints and a docstring describing the function's purpose, inputs, and expected output. Furthermore, the function adheres to Python's "PEP 8" style guide, ensuring that code is readable and consistent.

Note: The function assumes that the text given is a string. If you pass in a different type, the function may raise a TypeError or return an unexpected result.