def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    # Find the longest palindromic suffix
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1
    # Find the longest non-palindromic prefix before that suffix
    j = 0
    while not is_palindrome(s[j:i]):
        j += 1
    # Construct the answer
    palindrome = s[i:]+s[j:i][::-1]
    return palindrome