

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

    def is_palindrome_helper(string: str) -> bool:
        return string == string[::-1]

    def find_longest_postfix_palindrome(string: str) -> str:
        """
        Find the longest postfix of a supplied string that is a palindrome.
        >>> find_longest_postfix_palindrome('')
        ''
        >>> find_longest_postfix_palindrome('abcd')
        'cd'
        >>> find_longest_postfix_palindrome('cabcd')
        'c'
        >>> find_longest_postfix_palindrome('cat')
        't'
        >>> find_longest_postfix_palindrome('cata')
        'a'
        """

        def is_palindrome_helper(string: str) -> bool:
            return string == string[::-1]

        def find_palindrome_helper(string: str) -> str:
            if not string:
                return ''
            if is_palindrome_
