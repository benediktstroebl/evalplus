def is_palindrome(s: str) -> bool:
    """ Test if a string is a palindrome """
    return s == s[::-1]
def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with the supplied string.
    """
    if is_palindrome(string):
        return string
    # Find the longest palindromic suffix
    i = string.rfind(string[::-1])
    # i is the index of the palindromic suffix, reverse it (to make it a prefix)
    prefix = string[:i][::-1]
    # Replace the palindromic suffix with the reverse of the prefix
    newstr = string.replace(string[i:i+1], prefix)
    return newstr