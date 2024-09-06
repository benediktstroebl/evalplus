def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with string s """
    if not s:
        return s

    # find the position of the longest palindromic suffix
    psi = len(s)
    for i in range(1, len(s)):
        if is_palindrome(s[i:]) and len(s[i:]) > psi:
            psi = i

    # extract the palindromic suffix
    palindrome_suffix = s[psi:]

    # find the position of the nearest palindromic prefix
    pp = psi
    for i in range(psi - 1, -1, -1):
        if is_palindrome(s[:i]) and len(s[:i]) > pp:
            pp = i

    # extract the reverse of the palindromic prefix
    reverse_palindrome_prefix = s[pp:][::-1]

    return s[:pp] + reverse_palindrome_prefix + palindrome_suffix