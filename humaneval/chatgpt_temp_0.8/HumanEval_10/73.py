def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if not string:
        return ''

    # Find the longest palindromic suffix of the string
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            # Append the reverse of the non-palindromic prefix to the palindromic suffix
            return string + string[:len(string)-i][::-1]

    # If the whole string is not palindromic, append the reverse of the whole string
    return string + string[:-1][::-1]
