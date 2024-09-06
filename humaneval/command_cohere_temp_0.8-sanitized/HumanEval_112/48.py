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