def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix.
    i = string.rfind(string[::-1])
    if i == -1:
        return string+string[0:]

    # Find the shortest non-palindromic prefix.
    j = string.find(string[i:i+2], 1)
    if j == -1:
        return string[i:] + string[0:i][::-1]
    return string[i:] + string[0:j][::-1]