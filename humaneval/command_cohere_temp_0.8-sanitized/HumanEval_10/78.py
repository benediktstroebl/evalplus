def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    if not s:
        return s

    # Find the position of the longest palindrome suffix in s
    i = len(s) - 1
    while i >= 0 and not is_palindrome(s[i:]):
        i -= 1

    # Extend the string with the reverse of the prefix up to the palindrome suffix
    j = i
    while not is_palindrome(s[:j]):
        j -= 1
    return make_palindrome(s[:j] + s[i:i+j][::-1] + s[j:])