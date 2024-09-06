def is_palindrome(s: str) -> bool:
    """Returns true if string s is a palindrome, false otherwise."""
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """Returns the shortest palindrome that begins with the supplied string s."""
    if not s:
        return s

    # Find the longest palindromic suffix in s
    i = len(s) - 1
    while i >= 0 and not is_palindrome(s[i:]):
        i -= 1

    # Extract the palindromic suffix
    palindrome_suffix = s[i:] if i >= 0 else s

    # Find the longest common prefix of the normal and reversed strings
    j = 0
    while j < len(s) and s[j:] == palindrome_suffix[::-1]:
        j += 1

    # Extract the common prefix and palindromic suffix
    prefix = s[:j] if j < len(s) else s
    new_s = prefix + palindrome_suffix[::-1]

    return make_palindrome(new_s)