```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): Input string to check

    Returns:
    bool: True if the string is a palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(' ', '').lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example use cases
if __name__ == "__main__":
    print(is_palindrome(''))  # True
    print(is_palindrome('aba'))  # True
    print(is_palindrome('aaaaa'))  # True
    print(is_palindrome('zbcd'))  # False
    print(is_palindrome('A man a plan a canal Panama'))  # True
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes any spaces from the string and converts it to lowercase. Then it compares the cleaned string with its reverse. If they are the same, the function returns `True`; otherwise, it returns `False`. The example use cases demonstrate how to use the function.