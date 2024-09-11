```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(""))  # True
    print(is_palindrome("aba"))  # True
    print(is_palindrome("aaaaa"))  # True
    print(is_palindrome("zbcd"))  # False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It removes all spaces from the string, converts it to lowercase, and then compares the cleaned string with its reverse. If they are the same, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`. The script also includes test cases to verify the correctness of the function.