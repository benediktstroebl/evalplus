def is_palindrome(s: str) -> bool:
    """Returns true if string s is a palindrome, false otherwise."""
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """Returns the shortest palindrome string that begins with the input string s."""
    if not s:
        return s

    # find the location of the longest palindrome suffix
    i = len(s) - 1
    while i >= 0 and not is_palindrome(s[i:]):
        i -= 1

    # extract the palindrome suffix
    palindrome_suffix = s[i:]
    s = s[:i]

    # find the reverse complement of the prefix
    j = len(s) - 1
    complement = s[j:][::-1]
    s = s[:j]

    return s + complement + palindrome_suffix