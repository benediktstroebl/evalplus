def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with string s """
    if not s:
        return s

    # find the longest palindromic suffix
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1

    # find the shortest non-palindromic prefix
    j = 0
    while is_palindrome(s[:j]+s[i:i+j]):
        j += 1

    return make_palindrome(s[:j] + s[i:i+j][::-1] + s[j+1:])