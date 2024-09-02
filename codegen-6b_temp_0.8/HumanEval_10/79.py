

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
    if string == '':
        return ''

    all_substrings = get_all_substrings(string)

    longest_palindrome = ''
    for substring in all_substrings:
        if is_palindrome(substring):
            if len(longest_palindrome) < len(substring):
                longest_palindrome = substring

    if longest_palindrome == '':
        return string
    else:
        return longest_palindrome + string[::-1]

