def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome that begins with the supplied string s """
    if not s:
        return s

    # find the location of the longest palindrome suffix
    j = len(s) - 1
    while j >= 0 and not is_palindrome(s[j:]):
        j -= 1

    if j == -1:
        return s

    # reverse the prefix up to the palindrome suffix, and append to s
    p = s[:j] + s[j:][::-1]
    return p + make_palindrome(p)