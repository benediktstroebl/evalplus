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