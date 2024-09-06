def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s, or an empty string if s is already a palindrome """
    if is_palindrome(s):
        return s

    # Find the longest palindromic suffix of s
    i = len(s) - 1
    while i > 0 and s[i] == s[i+1]:
        i -= 1

    if i == 0:
        return s + s[i:]

    # Find the shortest non-palindromic prefix of s
    j = 0
    while s[j] == s[i]:
        j += 1

    return s[j:] + s[i:i+j][::-1]