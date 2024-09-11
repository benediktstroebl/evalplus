```python
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    
    A palindrome is a string that reads the same backwards as forwards.
    This function is case sensitive and considers spaces and punctuation as characters.
    
    Parameters:
    text (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    
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
    # Remove any leading or trailing whitespace
    text = text.strip()
    
    # Compare the string with its reverse
    return text == text[::-1]

# Example usage:
if __name__ == "__main__":
    print(is_palindrome(''))  # Expected output: True
    print(is_palindrome('aba'))  # Expected output: True
    print(is_palindrome('aaaaa'))  # Expected output: True
    print(is_palindrome('zbcd'))  # Expected output: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It uses Python's slicing feature to reverse the string and then compares it with the original string. If they are the same, it returns True; otherwise, it returns False. The example usage at the end demonstrates how to use this function.