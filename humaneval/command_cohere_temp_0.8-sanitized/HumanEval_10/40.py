def is_palindrome(s: str) -> bool:
    """Returns True if string s is a palindrome, False otherwise."""
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """Returns the shortest palindrome that starts with the input string s."""
    if not s:
        return s

    # Find the longest palindromic suffix in the input string
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1

    # Extract the palindromic suffix
    palindrome_suffix = s[i:]

    # Find the longest string that precedes the palindromic suffix and reverse it
    j = 0
    while not is_palindrome(s[:i][::-1] + s[j:i]):
        j += 1

    prefix = s[j:i][::-1]
    return s[:i] + prefix + palindrome_suffix