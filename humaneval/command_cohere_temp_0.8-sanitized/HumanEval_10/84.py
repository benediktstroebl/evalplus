import re
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    palindrome = re.sub(r'(.)\1+', r'\1\1', string)
    return palindrome[:1] + palindrome[::-1][1:]