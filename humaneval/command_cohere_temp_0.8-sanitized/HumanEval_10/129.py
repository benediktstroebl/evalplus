def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix.
    i = string.rfind(string[::-1])
    if i == -1:
        return string + string[0:]

    # Find the closest prefix to the suffix that forms a palindrome.
    j = string.rfind(string[:i][::-1])
    if j == -1:
        return string + string[0:]

    return string[:j] + string[i:] + string[:j][::-1]