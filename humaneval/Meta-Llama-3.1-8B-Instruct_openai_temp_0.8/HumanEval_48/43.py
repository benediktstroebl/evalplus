```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The input string to check

    Returns:
    bool: True if the string is a palindrome, False otherwise

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
```

This function works by first removing any non-alphanumeric characters from the input string and converting it to lowercase. This is done to ensure that the function is case-insensitive and ignores any spaces, punctuation, or other non-alphanumeric characters. 

Then it checks if the cleaned string is equal to its reverse. If they are equal, the function returns True, indicating that the original string is a palindrome. Otherwise, it returns False. 

The `[::-1]` syntax is used to reverse the string. It tells Python to start at the end of the string and end at position 0, move with the step -1 which means one step backwards. 

This function can be used to check if any string is a palindrome, regardless of case or non-alphanumeric characters.