```python
def reverse_delete(s, c):
    """
    Deletes characters in 's' that are also in 'c', and checks if the remaining string is a palindrome.
    
    Args:
    - s (str): Input string.
    - c (str): String of characters to delete from 's'.
    
    Returns:
    - tuple: (str, bool): The modified string and a boolean indicating whether it's a palindrome.
    """
    modified_s = [x for x in s if x not in c]
    palindrome = modified_s == modified_s[::-1]
    return ''.join(modified_s), palindrome
```

This function constructs a new string by iterating through the characters in `s`, and uses a list comprehension to exclude characters that appear in the `c` string. The function then checks if the modified string is a palindrome by comparing it to its reverse using the slice notation `s[::-1]`, which effectively flips the string.

The final result is a tuple containing the modified string and a boolean that indicates whether it's a palindrome.