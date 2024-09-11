```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    
    Args:
        text (str): Input string to check
    
    Returns:
        bool: True if string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if is_palindrome(''):
    print("Empty string is a palindrome.")
if is_palindrome('aba'):
    print("aba is a palindrome.")
if is_palindrome('aaaaa'):
    print("aaaaa is a palindrome.")
if not is_palindrome('zbcd'):
    print("zbcd is not a palindrome.")
```

This Python script defines a function `is_palindrome` that checks if a given string is a palindrome. A palindrome is a string that reads the same backwards as forwards. The function removes non-alphanumeric characters from the string and converts it to lowercase before checking if it's a palindrome. It does this by comparing the cleaned string with its reverse. The test cases at the end of the script demonstrate that the function works correctly.