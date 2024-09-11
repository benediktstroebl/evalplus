### Palindrome Checker
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    Args:
        text (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove any whitespace and convert the string to lowercase
    cleaned_text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(''))  # True
    print(is_palindrome('aba'))  # True
    print(is_palindrome('aaaaa'))  # True
    print(is_palindrome('zbcd'))  # False
    print(is_palindrome('A man, a plan, a canal: Panama'))  # True
```

This script includes a function `is_palindrome` that checks if a given string is a palindrome. It cleans the input string by removing any whitespace and converting it to lowercase, then compares the cleaned string with its reverse using Python's slice notation `[::-1]`. If they match, the function returns `True`; otherwise, it returns `False`. The script includes test cases at the end to demonstrate its usage.