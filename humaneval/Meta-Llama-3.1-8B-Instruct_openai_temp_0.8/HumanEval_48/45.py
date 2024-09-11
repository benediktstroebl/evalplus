### Palindrome Checker
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The string to check

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
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example usage:
if __name__ == "__main__":
    print(is_palindrome(''))       # True
    print(is_palindrome('aba'))    # True
    print(is_palindrome('aaaaa'))  # True
    print(is_palindrome('zbcd'))   # False
```
This script defines a function `is_palindrome` that takes a string as input, removes any non-alphanumeric characters and converts it to lowercase. It then checks if the cleaned string is the same when reversed. The result is returned as a boolean value.