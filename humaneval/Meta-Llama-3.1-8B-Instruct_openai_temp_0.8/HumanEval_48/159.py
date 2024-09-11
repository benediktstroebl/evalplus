```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    
    A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
    
    Args:
    text (str): The input string to be checked.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    
    # Remove spaces and punctuation, and convert to lowercase
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```

This script defines a function `is_palindrome` that takes a string input, removes all non-alphanumeric characters, converts the string to lowercase, and checks if it's equal to its reverse. If they're equal, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`. The test cases at the end demonstrate the function's behavior on different inputs.