```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Remove spaces and convert to lowercase
    text = text.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return text == text[::-1]

# Example usage
if __name__ == "__main__":
    print(is_palindrome(""))  # True
    print(is_palindrome("aba"))  # True
    print(is_palindrome("aaaaa"))  # True
    print(is_palindrome("zbcd"))  # False
```

This Python script defines a function `is_palindrome` that checks whether a given string is a palindrome. It does this by removing any spaces from the string, converting it to lowercase, and then comparing it with its reverse. If the string is the same when read forwards and backwards, it's a palindrome, and the function returns `True`. Otherwise, it returns `False`. The example usage at the end demonstrates how to use this function with different input strings.