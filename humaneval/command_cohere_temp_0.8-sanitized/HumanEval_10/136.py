def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(string: str) -> str:
    """Returns the shortest palindrome string that starts with the input string."""
    if is_palindrome(string):
        return string
    # Find the longest palindromic suffix.
    i = len(string) - 1
    while i > 0 and not is_palindrome(string[-i:]):
        i -= 1
    # Find the longest non-palindromic prefix before the palindromic suffix.
    j = 0
    while not is_palindrome(string[j:i]):
        j += 1
    return make_palindrome(string[:j] + string[i:][::-1])