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