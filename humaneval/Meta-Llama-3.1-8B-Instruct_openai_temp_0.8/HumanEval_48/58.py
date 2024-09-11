### Palindrome Checker
#### Python Script
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    Args:
    text (str): Input string to check

    Returns:
    bool: True if the string is a palindrome, False otherwise

    Examples:
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Remove spaces and convert to lowercase
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example usage
if __name__ == "__main__":
    print(is_palindrome(""))  # True
    print(is_palindrome("aba"))  # True
    print(is_palindrome("aaaaa"))  # True
    print(is_palindrome("zbcd"))  # False
```
This script defines a function `is_palindrome` that checks if a given string is a palindrome. It works by removing non-alphanumeric characters and spaces, converting the string to lowercase, and then comparing it with its reverse. The function returns `True` if the string is a palindrome and `False` otherwise. The script includes example usage to demonstrate its functionality.