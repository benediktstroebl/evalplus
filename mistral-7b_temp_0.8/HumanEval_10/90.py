

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
    s = string
    ls = len(s)

    def _find_longest_palindromic_suffix(string: str) -> int:
        """ Find the longest palindromic suffix of string """
        p_suffix = 0
        p_len = 1

        for i in range(1, ls):
            if not is_palindrome(string[i-p_len:i]):
                p_suffix = i
                p_len = 1
                continue
            p_len += 1
        return p_suffix, p_len

    def _find_longest_palindromic_prefix(string: str) -> int:
        """ Find the longest palindromic prefix of string """
        p_prefix = 0
        p_len = 0

        for i in range(ls-1, -1, -1):
            if not is_palindrome(string[i:i+p_len]):
                p_prefix = i+1
                p_len = 0
