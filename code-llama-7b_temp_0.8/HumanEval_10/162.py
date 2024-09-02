

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

    def get_prefix(string: str) -> str:
        """ Return the longest prefix that is a palindrome """
        for i in range(len(string)):
            if not is_palindrome(string[:i + 1]):
                return string[:i]
        return string

    def get_suffix(string: str) -> str:
        """ Return the longest suffix that is a palindrome """
        for i in range(len(string)):
            if not is_palindrome(string[i:]):
                return string[i:]
        return string

    def get_palindrome(string: str) -> str:
        """ Return the palindrome suffix """
        suffix = get_suffix(string)
        if len(suffix) == 0:
            return ''
        return suffix[0] * (len(suffix) - 1)

    def get_prefix_len(string: str) -> int:
        """ Return the length of the longest palindromic prefix """
        i = 0
        while (i + 1 < len(string)) and is_palindrome(string[i: i + 2]):
            i += 1
        return i

    def get_suffix_len(string: str) -> int:
        """ Return the length of the longest palindromic suffix """
        i = len(string) - 1
        while (i - 1 >= 0) and is_palindrome(string[i - 1: i + 1]):
            i -= 1
        return len(string) - i - 1

    prefix = get_prefix(string)
    palindrome = get_palindrome(string)
    suffix = get_suffix(string)

    if len(palindrome) % 2 == 0:
        new_palindrome = palindrome[len(palindrome) // 2:] + palindrome[:len(palindrome) // 2]
    else:
        new_palindrome = palindrome[len(palindrome) // 2 + 1:] + palindrome[len(pal
