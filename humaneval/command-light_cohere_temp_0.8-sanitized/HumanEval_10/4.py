def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return ""

    # Algorithm idea:
    # Find the longest palindrome prefix
    # Append reverse of prefix and suffix to form palindrome
    # Returns the shortest palindrome
    prefix = string[:0:-1]