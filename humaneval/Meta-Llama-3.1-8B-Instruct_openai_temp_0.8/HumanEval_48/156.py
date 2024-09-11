```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    A palindrome is a string that reads the same backward as forward.

    Args:
    text (str): The input string to be checked.

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
    # Remove any white spaces and convert to lower case
    cleaned_text = text.replace(" ", "").lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(""))  # Expected: True
    print(is_palindrome("aba"))  # Expected: True
    print(is_palindrome("aaaaa"))  # Expected: True
    print(is_palindrome("zbcd"))  # Expected: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It removes any white spaces from the string, converts it to lower case, and then compares it with its reverse. If they are the same, the function returns `True`; otherwise, it returns `False`. The test cases at the end verify the function's correctness.