```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome ignoring case, non-alphanumeric characters, and spaces.
    
    Args:
        text (str): The input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]

print(is_palindrome(""))  # True
print(is_palindrome("aba"))  # True
print(is_palindrome("aaaaa"))  # True
print(is_palindrome("zbcd"))  # False
```

This script uses Python's built-in string slicing (`[::-1]`) to reverse the string, and a generator expression to clean the input string. It removes non-alphanumeric characters and converts the string to lowercase to ignore case differences.