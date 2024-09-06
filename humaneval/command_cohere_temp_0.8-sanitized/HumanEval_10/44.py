def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind(string[::-1])
    if i == -1:
        return string + string[0:]

    # Extend the string with the reverse of the prefix
    return string + string[:i][::-1]