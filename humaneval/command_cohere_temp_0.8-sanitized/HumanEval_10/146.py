def is_palindrome(s: str) -> bool:
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    if not s:
        return s

    # find the longest palindrome suffix
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1

    # reverse the prefix up to the palindrome suffix
    s_prefix = s[:i]
    s = s_prefix + s[i:i][::-1]

    return s