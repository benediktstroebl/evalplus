def is_palindrome(s: str) -> bool:
    """Returns true if string s is a palindrome"""
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """Returns the shortest palindrome string that starts with s"""
    # Find the longest palindromic suffix.
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1
    # Find the corresponding palindromic prefix.
    j = 0
    while not is_palindrome(s[:j] + s[i:i+j]):
        j += 1
    return s[:j] + s[i:i+j][::-1]