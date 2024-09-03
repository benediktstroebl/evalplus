def is_palindrome(text: str):
    """
    Checks if the given string is a palindrome.
    This function uses a simple algorithm to compare the first and last characters 
    of the string and iteratively move towards the center.
    Args:
        text (str): String to check for palindrome property.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True