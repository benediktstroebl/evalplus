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
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(''))  # Expected: True
    print(is_palindrome('aba'))  # Expected: True
    print(is_palindrome('aaaaa'))  # Expected: True
    print(is_palindrome('zbcd'))  # Expected: False
    print(is_palindrome('A man, a plan, a canal: Panama'))  # Expected: True
```

This script defines a function `is_palindrome` that checks whether a given string is a palindrome. It removes non-alphanumeric characters and converts the string to lowercase before comparing it with its reverse. If the string is the same when reversed, it is a palindrome.