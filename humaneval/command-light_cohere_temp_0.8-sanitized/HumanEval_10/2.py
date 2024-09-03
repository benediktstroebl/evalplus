def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string."""
    if not string:
        return ''
    # Find the longest postfix of supplied string that is a palindrome.