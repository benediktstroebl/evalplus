def is_palindrome(s: str) -> bool:
    """Returns true if string s is a palindrome, false otherwise."""
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """Returns the shortest palindrome string that starts with s."""
    if not s:
        return s

    # Find the longest palindromic suffix.
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1

    # Find the longest non-palindromic prefix before the palindromic suffix.
    j = 0
    while not is_palindrome(s[j:i+1]):
        j += 1

    # Reverse the non-palindromic prefix and concatenate.
    return make_palindrome(s[j:i+1][::-1]) + s[:j]