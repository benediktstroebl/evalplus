def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # Find the longest palindromic suffix.
    i = string.rfind(string[::-1])
    return f"{string[:i]}{string[i:i+2][::-1]}{string[i+2:]}"