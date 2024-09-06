def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind(''.join(reversed(string)))

    # Extend the string with the reversed prefix until a palindrome is found
    new_string = string[i:] + ''.join(reversed(string[:i]))

    return make_palindrome(new_string)