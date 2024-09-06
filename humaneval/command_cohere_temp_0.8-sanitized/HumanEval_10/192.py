def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind(''.join(filter(str.isalnum, string)))
    if i == -1:
        return string
    suffix = string[i:]
    reversed_prefix = suffix[::-1]

    # Remove the palindromic suffix from the original string
    prefix = string[:i]
    return f'{prefix}{reversed_prefix}{"".join(filter(str.isalnum, string[i+1:]))}'