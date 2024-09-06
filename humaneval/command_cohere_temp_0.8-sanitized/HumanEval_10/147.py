def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s, or an empty string if s is already a palindrome """
    if is_palindrome(s):
        return s

    # Find the longest palindromic suffix of s
    i = len(s) - 1
    while i > 0 and s[i] != s[i-1]:
        i -= 1
    if i == 0:
        return make_palindrome(s + s)

    # Find the longest non-palindromic prefix of the suffix
    j = i
    while s[j] == s[i]:
        j -= 1
    if s[j] == s[i]:
        return make_palindrome(s[j:] + s[i:-i] + s[j:])

    return make_palindrome(s[i:] + s[:i])