def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    if not s:
        return s

    # find the position of the longest palindromic suffix
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1

    # extract the palindromic suffix
    palindrome = s[i:]
    s = s[:i]

    # find the position of the matching palindromic prefix
    j = 0
    while not is_palindrome(s[:j] + palindrome):
        j += 1

    return s[:j] + palindrome