def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix.
    i = string.rfind(string[::-1])
    if i == -1:
        return string + string[0:]

    # Find the reverse of the prefix before the palindromic suffix.
    j = string.rfind(string[:i], 0, i - 1)
    if j == -1:
        return string[i:] + string[:i]
    return string[i:] + string[j+1:]