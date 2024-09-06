def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    # find the longest palindrome suffix
    palindrome_idx = len(s) - len(reversed(s[:-1])) - 1
    # reverse the prefix up to the palindrome suffix
    s = s[:palindrome_idx] + s[palindrome_idx:][::-1]
    return s