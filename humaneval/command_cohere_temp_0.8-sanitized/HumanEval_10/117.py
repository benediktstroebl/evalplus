def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    # Find the longest palindrome suffix
    i = len(s) - 1
    while i > 0 and is_palindrome(s[i:]):
        i -= 1

    # Find the longest non-palindrome prefix before that suffix
    j = 0
    while not is_palindrome(s[:j]+s[i:]):
        j += 1

    # Construct the answer by chopping the non-palindrome prefix,
    # then appending its reverse to the palindrome suffix
    return s[j:i]+s[j:j+len(s[j:i])[::-1]]