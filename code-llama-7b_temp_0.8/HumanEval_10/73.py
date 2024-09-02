

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

    # Reverse supplied string
    reversed_string = string[::-1]

    # Find the longest palindromic suffix of the supplied string
    palindrome_suffix = find_longest_palindrome_suffix(string)

    # If there is no palindromic suffix, return a concatenation of the reversed supplied string and the supplied string
    if not palindrome_suffix:
        return reversed_string + string

    # Find the longest prefix of the supplied string that is a palindrome
    palindrome_prefix = find_longest_palindrome_prefix(string)

    # If there is no palindromic prefix, return the reversed string
    if not palindrome_prefix:
        return reversed_string

    # Find the longest palindrome that starts with a supplied string
    palindrome = find_longest_palindrome(string)

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return palindrome + reversed_string[:-len(palindrome_suffix)]

