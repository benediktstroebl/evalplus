def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    # Find the longest palindrome suffix ending at i
    i = len(s) - 1
    while i > 0 and is_palindrome(s[i:]) != True:
        i -= 1
    # Find the longest palindrome prefix starting at j
    j = 0
    while j < len(s) // 2 and is_palindrome(s[:j]+s[i:j-1]) != True:
        j += 1
    return s[:j] + s[i:j-1][::-1] + s[j+1:]