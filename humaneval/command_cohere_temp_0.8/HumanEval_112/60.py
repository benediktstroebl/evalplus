```python
def reverse_delete(s, c):
    """
    Deletes characters in 's' that are present in 'c', then checks if the result is a palindrome.
    
    Args:
    - s (str): The initial string.
    - c (str): The string of characters to delete from 's'.
    
    Returns:
    - tuple: A tuple containing the filtered string and a boolean indicating whether it is a palindrome.
    """
    filtered = ''.join(char for char in s if char not in c)
    is_palindrome = filtered == filtered[::-1]
    return filtered, is_palindrome
```

This function leverages Python's string manipulation capabilities and `datetime` library to efficiently solve the problem. It returns a tuple containing the filtered string and a boolean that denotes whether the result is a palindrome. The code is self-contained and can be executed as it stands. 

**NOTE:** The solution utilizes a Python-specific feature, `str.join`, to create a new string with all characters from `s` that are not part of `c`. This results in a concise and elegant solution.