```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Split the string into individual characters and reverse the list.
    char_list = text.split()
    reversed_char_list = char_list[::-1]
    
    # Check if the original string is equal to the reversed string.
    return text == ''.join(reversed_char_list)
```