def is_palindrome(s):
    return s == s[::-1]
def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string."""
    def palindrome_builder(s, idx):
        if idx >= len(s):
            return s
        if is_palindrome(s[idx:]):
            return palindrome_builder(s, idx + 1)
        return palindrome_builder(s[:idx] + s[idx][::-1], idx + 1)

    return palindrome_builder(string, 0)