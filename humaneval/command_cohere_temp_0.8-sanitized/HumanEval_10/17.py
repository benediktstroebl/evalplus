def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix.
    i = string.rfind(string[::-1])
    if i == -1:
        return string + string[0:]

    # Find the longest non-palindromic prefix before the palindromic suffix.
    j = i - 1
    while string[j:i] == string[j:i][::-1]:
        j -= 1
    if j < 0:
        return string

    return make_palindrome(string[:j] + string[i:])