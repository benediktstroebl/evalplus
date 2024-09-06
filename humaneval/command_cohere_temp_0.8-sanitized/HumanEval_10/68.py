def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s, or an empty string if s is already a palindrome """
    if is_palindrome(s):
        return s

    # Find the longest palindrome suffix in the string
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1

    # Find the shortest non-palindrome prefix before the palindrome suffix
    j = 0
    while not is_palindrome(s[:j]+s[i:]):
        j += 1

    # Construct the shortest palindrome that starts with s
    result = s[:j] + s[i:i+1][::-1]
    return result