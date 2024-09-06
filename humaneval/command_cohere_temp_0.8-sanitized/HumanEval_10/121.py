import re
def make_palindrome(s: str) -> str:
    """Returns the shortest palindrome string that starts with s"""
    palindrome = s + re.sub(r'(.)\1*', r'\1\1', s)[::-1]
    return palindrome