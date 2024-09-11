```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
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
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        '',
        'aba',
        'aaaaa',
        'zbcd'
    ]
    
    for text in test_cases:
        print(f"{text}: {is_palindrome(text)}")
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It removes non-alphanumeric characters and converts the string to lowercase before comparing it with its reverse. The script also includes test cases to demonstrate the function's behavior.