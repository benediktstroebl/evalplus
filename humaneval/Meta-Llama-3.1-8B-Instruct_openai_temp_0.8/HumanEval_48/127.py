```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.
    
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
    print(is_palindrome(''))  # True
    print(is_palindrome('aba'))  # True
    print(is_palindrome('aaaaa'))  # True
    print(is_palindrome('zbcd'))  # False
```

In this script, the `is_palindrome` function first removes non-alphanumeric characters from the input string and converts it to lowercase to ignore case differences. Then it checks if the cleaned string is equal to its reverse (`cleaned_text[::-1]`). This is done using Python's slice notation, which allows us to create a reversed copy of the string. The function returns `True` if the string is the same forwards and backwards, and `False` otherwise.