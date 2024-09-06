def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind('.{}'.format(string[::-1]))
    if i == -1:
        return string+string[::-1]

    # Reverse the prefix before the palindromic suffix and return
    return string[:i]+string[i:i+1][::-1]+string[i+1:]