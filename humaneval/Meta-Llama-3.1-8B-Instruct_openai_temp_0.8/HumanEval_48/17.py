```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.
    
    A palindrome is a string that reads the same backwards as forwards.
    
    :param text: The input string to check.
    :return: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]

# Example usage:
print(is_palindrome(""))  # True
print(is_palindrome("aba"))  # True
print(is_palindrome("aaaaa"))  # True
print(is_palindrome("zbcd"))  # False
```

This script defines a function `is_palindrome` that takes a string as input, removes non-alphanumeric characters, and checks if the cleaned string is equal to its reverse. The function returns `True` if the string is a palindrome and `False` otherwise. The example usage at the end demonstrates how to use this function with the provided test cases.