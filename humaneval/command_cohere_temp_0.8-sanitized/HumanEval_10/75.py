def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(string: str) -> str:
    """Returns the shortest palindrome string that starts with the input string."""
    if is_palindrome(string):
        return string
    # Find the longest palindrome suffix.
    suffix_start = len(string) // 2
    palindrome_suffix = string[suffix_start:][::-1]
    if string + palindrome_suffix != string[::-1]:
        return make_palindrome(string + palindrome_suffix)
    # Find the shortest non-palindrome prefix of the string right before the palindrome suffix.