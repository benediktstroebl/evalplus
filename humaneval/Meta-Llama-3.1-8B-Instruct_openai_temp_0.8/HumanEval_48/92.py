```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    A string is considered a palindrome if it reads the same backwards as forwards.
    The function is case insensitive and considers spaces and punctuation as non-alphanumeric characters.

    Args:
        text (str): The string to check for palindrome.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(""))  # True
    print(is_palindrome("aba"))  # True
    print(is_palindrome("aaaaa"))  # True
    print(is_palindrome("zbcd"))  # False
    print(is_palindrome("A man a plan a canal Panama"))  # True
    print(is_palindrome("Not a palindrome"))  # False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first cleans the string by removing non-alphanumeric characters and converting it to lowercase. Then it compares the cleaned string with its reverse. If they are the same, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`. The script includes test cases to demonstrate the function's behavior.