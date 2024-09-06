def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # using str.replace to efficiently insert reverse of prefix to create palindrome
    return string + string[1:].replace(string[:1], string[::-1][1:])