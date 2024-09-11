```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    
    A palindrome is a string that reads the same backwards as forwards.
    
    Args:
        text (str): The input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    text = ''.join(e for e in text if e.isalnum()).lower()  # Remove non-alphanumeric characters and convert to lowercase
    return text == text[::-1]  # Compare the string with its reverse

# Test cases
if __name__ == "__main__":
    print(is_palindrome(""))  # Expected output: True
    print(is_palindrome("aba"))  # Expected output: True
    print(is_palindrome("aaaaa"))  # Expected output: True
    print(is_palindrome("zbcd"))  # Expected output: False
```
This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes all non-alphanumeric characters and converts the string to lowercase to ensure the comparison is case-insensitive. Then it compares the resulting string with its reverse to determine if it's a palindrome. The test cases at the end demonstrate the function's usage.