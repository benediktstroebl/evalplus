def is_palindrome(s):
    return s == s[::-1]
def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string."""
    def palindrome_builder(s, prefix, suffix):
        if is_palindrome(s):
            return s
        if not s:
            return s
        return palindrome_builder(s[1:], prefix + s[0], suffix + s[0])

    return palindrome_builder(string, string, '')