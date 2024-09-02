

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
    # Keep only letters
    string = ''.join(filter(str.isalpha, string))
    # If string is already palindrome, just return it
    if is_palindrome(string):
        return string

    # Start from the back and keep finding palindromic suffixes
    # 'cata', 'ata', 'ta'
    for i in reversed(range(len(string) // 2 + 1)):
        # Check if the suffix is palindrome
        if is_palindrome(string[i:]):
            # Add prefix and reverse it
            return string + string[:i][::-1]

    return string

