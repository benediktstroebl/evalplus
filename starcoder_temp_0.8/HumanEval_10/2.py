

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

    def longest_palindromic_postfix(string: str) -> str:
        """ Find the longest postfix of supplied string that is a palindrome. """
        longest_palindrome = ''
        for i in range(len(string)):
            if is_palindrome(string[-i:]):
                longest_palindrome = string[-i:]

        return longest_palindrome

    postfix = longest_palindromic_postfix(string)

    return string + postfix[::-1]

