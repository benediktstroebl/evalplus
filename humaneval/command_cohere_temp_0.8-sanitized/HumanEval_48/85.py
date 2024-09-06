def is_palindrome(text: str):
    """
    Checks if a given string is a palindrome.
    """
    # Your code here :)
    if text == text[::-1]:
        return True
    else:
        return False