

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
    def get_shortest_palindromic_suffix(string: str) -> str:
        suffix_len = 0
        for i in range(len(string)):
            if is_palindrome(string[i:]):
                suffix_len = i
        return string[:-suffix_len]

    string_prefix = get_shortest_palindromic_suffix(string)
    return string_prefix + string_prefix[::-1]

