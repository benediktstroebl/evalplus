Here's a Python script with a self-contained function that solves the problem of checking if a given string is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    
    Args:
        text (str): Text to be checked.
        
    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    # Convert text to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if the reversed text matches the original text
    return text == text[::-1]
```
This function uses a couple of tricks to make the palindrome check efficient:
1. It converts the input text to lowercase and removes all non-alphanumeric characters, which ensures that the check ignores punctuation, whitespace, and other non-alphanumeric characters.
2. It uses slicing with a reversed iterator to compare the original text with its reverse, which is a more efficient approach than manually reversing the string.

The function can be tested with the following calls:
```python
# Test if an empty string is a palindrome
print(is_palindrome(''))
# Test if a non-empty palindrome is a palindrome
print(is_palindrome('aba'))
# Test if a long string of same characters is a palindrome
print(is_palindrome('aaaaa'))
# Test if a non-palindrome is not a palindrome
print(is_palindrome('zbcd'))
```
The expected output will be:
```
True
True
True
False
```