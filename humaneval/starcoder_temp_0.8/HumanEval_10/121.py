

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
    if is_palindrome(string):
        return string

    # Find longest prefix that is a palindrome
    for i in range(len(string), 0, -1):
        prefix = string[:i]
        if is_palindrome(prefix):
            # Find shortest suffix that is a palindrome
            for j in range(i, len(string)):
                suffix = string[j:]
                if is_palindrome(suffix):
                    # Found a palindrome!
                    return prefix + string[i:j][::-1] + suffix

    return ""

