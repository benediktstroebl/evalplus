```python
def reverse_delete(s, c):
    """
    Deletes characters in 's' that are present in 'c', then checks if the resulting string is a palindrome.
    
    Args:
    - s (str): Input string.
    - c (str): String of characters to delete from 's'.
    
    Returns:
    - tuple: (str, bool): The modified string and a boolean indicating whether it is a palindrome.
    """
    deleted = ''.join([char for char in s if char not in c])
    palindrome = deleted == deleted[::-1]
    return deleted, palindrome
```

This function takes two strings, s, and c, as input. It removes characters from string s that are present in string c, effectively deleting them. After deleting these characters, the function checks whether the resulting string is a palindrome. A palindrome is a word, phrase, number, or sequence that reads the same backward as forward. Finally, the function returns a tuple containing the modified string and a boolean value indicating whether it is a palindrome.