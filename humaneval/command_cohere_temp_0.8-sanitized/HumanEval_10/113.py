def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the longest palindromic suffix.
    i = string.find_longest_match(string[::-1], 0, len(string) // 2)
    suffix = string[i:]

    # Find the character preceding the palindromic suffix.
    prefix = string[:i]

    return make_palindrome(prefix + suffix[::-1])