def is_palindrome(s: str) -> bool:
    """Returns True if string s is a palindrome, False otherwise."""
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """Returns the shortest palindrome that begins with the supplied string s."""
    if not s:
        return s

    # Find the longest palindromic suffix in the string.
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1

    # Extend the string with the reverse of the part before the palindromic suffix.
    ext = s[:i] + s[i:][::-1]
    return make_palindrome(ext) + s[i:]