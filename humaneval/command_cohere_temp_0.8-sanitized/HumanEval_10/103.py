def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # Find the longest palindromic suffix of the string:
    i = string.rfind(string[::-1]) # Corrected slice for reverse finding
    # Append the reverse of the corresponding prefix to the string:
    return string[:i] + string[i:][::-1]