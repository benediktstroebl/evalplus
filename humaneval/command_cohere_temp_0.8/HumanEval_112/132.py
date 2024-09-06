```python
def reverse_delete(s, c):
    """
    Deletes characters in 's' that are present in 'c', then checks if the resulting string is a palindrome.
    
    Args:
    - s (str): The original string.
    - c (str): The string of characters to delete from 's'.
    
    Returns:
    - tuple: A tuple containing the modified string and a boolean indicating whether it is a palindrome.
    """
    deleted = ''.join(char for char in s if char not in c)
    palindrome = deleted == deleted[::-1]
    return deleted, palindrome
```

This function employs two separate steps to solve the problem:
1. It creates a string `deleted` by filtering out the characters in `s` that are also present in `c`. This is achieved using a list comprehension, excluding these characters from the final string.
2. After creating the `deleted` string, it checks if this modified string is a palindrome by comparing it to its reverse (`deleted[::-1]`). If they are equal, the boolean `palindrome` is set to `True`; otherwise, it is set to `False`. 

The function returns these two values (`deleted` and `palindrome`) as a tuple to conform to the problem's requested output format. 

This solution adheres to the problem's guidelines and provides an efficient approach to tackle it.