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
    deleted = ''.join([c2 for c2 in s if c2 not in c])
    return deleted, deleted == deleted[::-1]
```

This function employs two separate lists iterations to clean the main string `s`:
1. One that collects all the characters in `s` that are NOT in the string `c` (let's call this list `bc`).
2. Another that deletes each character in `s` if it is ALSO in `c`.

After this preparation, the function returns a tuple containing the cleaned string and a boolean indicating whether it is a palindrome. The latter is determined by checking if the cleaned string is equal to its reverse (`s[::-1]`), which is a standard palindrome check.