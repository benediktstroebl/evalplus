def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind('.{}'.format(string[::-1]))
    if i == -1:
        return string

    # Reverse the prefix before the palindromic suffix and append it
    return make_palindrome(string[:i]) + string[i:][::-1]