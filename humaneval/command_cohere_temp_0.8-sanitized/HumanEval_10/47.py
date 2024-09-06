def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(string: str) -> str:
    """Returns the shortest palindrome string that begins with the supplied string """
    if is_palindrome(string):
        return string
    # Find the longest palindrome suffix.
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[-i-1:]):
        i -= 1
    # Find the shortest non-palindrome prefix.
    j = 0
    while j < len(string) // 2 and is_palindrome(string[j:j+len(string) // 2]):
        j += 1
    return make_palindrome(string[j:i+1] + string[::i-j-1])