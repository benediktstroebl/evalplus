def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # Find the longest palindromic suffix of the string
    i = string.rfind(string[::-1])
    # Extend the string with the reverse of the prefix up to the palindromic suffix
    return string[:i] + string[i:][::-1]