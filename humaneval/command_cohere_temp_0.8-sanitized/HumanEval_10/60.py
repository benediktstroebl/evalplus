def is_palindrome(s: str) -> bool:
    """Test if a string is a palindrome."""
    return s == s[::-1]
def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with the supplied string."""
    # Find the longest palindromic suffix.
    i = len(string) - 1
    while i > 0 and is_palindrome(string[i:]):
        i -= 1
    # Find the corresponding palindromic prefix.
    j = 0
    while is_palindrome(string[:j]+string[i:i+j]):
        j += 1
    return string[:j] + string[i:i+j][::-1]