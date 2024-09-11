### Palindrome Checker
#### Python Script

```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    
    Args:
    text (str): The input string to check
    
    Returns:
    bool: True if the string is a palindrome, False otherwise
    
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    return text == text[::-1]


# Example usage:
if __name__ == "__main__":
    test_cases = ["", "aba", "aaaaa", "zbcd"]
    for test_case in test_cases:
        print(f"{test_case}: {is_palindrome(test_case)}")
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It uses Python's slicing feature to compare the string with its reverse. The script also includes example usage to demonstrate the function's behavior with different test cases.