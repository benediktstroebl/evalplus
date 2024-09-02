

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Remove spaces and lowercase all text
    text = ''.join(text.split()).lower()
    # Check if text is an even length string
    if len(text) % 2 == 0:
        # Reverse the even indexed characters and compare to the original string
        return text[:len(text) // 2] == text[len(text) - 1:len(text) // 2 - 1:-1]
    # If not, return false
    return False

