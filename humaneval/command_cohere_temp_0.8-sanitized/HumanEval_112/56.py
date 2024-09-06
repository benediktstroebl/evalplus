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