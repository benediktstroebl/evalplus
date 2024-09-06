def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    if not s:
        return s

    # Find the position of the longest palindromic suffix in s
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1

    # Extract the palindromic suffix (reverse the part before i and concatenate to s)
    palindromic_suffix = s[i:i+1] + s[i:-i-1][::-1]
    s = s[:-i-1] + palindromic_suffix

    return s