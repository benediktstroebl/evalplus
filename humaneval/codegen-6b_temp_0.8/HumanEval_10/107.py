

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    # split the string into chunks of size at most 2
    chunks = [string[i:i + 2] for i in range(len(string) - 1)]

    for prefix, suffix in chunks:
        # ignore characters that are not letters
        if prefix.isalpha() and suffix.isalpha():
            # check if prefix is a palindrome and suffix is a palindrome
            if is_palindrome(prefix) and is_palindrome(suffix):
                return prefix + suffix[::-1]
    return string

