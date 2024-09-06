def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]
def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome that begins with the supplied string s """
    if not s:
        return s

    # Find the location of the longest palindromic suffix
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1

    # Extract the reverse of the prefix up to the palindromic suffix
    prefix = s[:i]
    reverse_prefix = prefix[::-1]

    # Append the reverse prefix to the string to make a palindrome
    return f"{s[i:]}{reverse_prefix}"