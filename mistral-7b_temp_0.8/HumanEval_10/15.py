

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
    if not string:
        return ''
    if is_palindrome(string):
        return string
    # Now we know that the string has a non-palindromic prefix and a palindromic suffix
    palindrome_suffix = string[::-1]
    palindrome_suffix_index = 0
    # Find the longest palindrome suffix
    while palindrome_suffix_index < len(string) and palindrome_suffix_index < len(palindrome_suffix) and is_palindrome(string[palindrome_suffix_index:]):
        palindrome_suffix_index += 1
    # Prepend the reverse of the non-palindromic prefix
    palindrome_prefix = string[:palindrome_suffix_index][::-1]
    return palindrome_prefix + palindrome_suffix

