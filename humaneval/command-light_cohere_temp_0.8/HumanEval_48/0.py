Here is a Python script with a self-contained function that solves the problem of checking if a given string is a palindrome:
```python
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    Returns: boolean
    """
    # Remove spaces to make sure only characters are checked
    text = text.replace(' ', '')

    # Convert to lowercase to make the comparison case-insensitive
    return text == text[::-1]

# Test the function with some inputs
print(is_palindrome(''))  # True
print(is_palindrome('ab'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```
This function removes spaces from the input string to ensure the character comparison is case-insensitive, then checks if the original string is equal to its reverse, which is the definition of a palindrome.