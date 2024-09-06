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
This function removes any non-alphanumeric characters and converts the text to lowercase to make the comparison case-insensitive. Then, it compares the original text with its reverse to determine if it's a palindrome. The function includes type hints to indicate the expected input and return type, and the docstring provides an explanation of the function's purpose, inputs, and expected output. 

To use this function, you can simply call it with a string argument like this:
```python
print(is_palindrome('Racecar'))  # Outputs: True
print(is_palindrome('Hello'))  # Outputs: False
```
This will print `True` for a palindrome string and `False` for a non-palindrome string.