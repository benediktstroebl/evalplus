

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
    def palindromic_postfix(string: str) -> Tuple[int, int]:
        """ Find the longest palindromic postfix of a given string """
        for i in range(len(string)//2, 0, -1):
            if is_palindrome(string[-i:]):
                return len(string) - i, i
        return 0, 0

    left, right = palindromic_postfix(string)
    if left == 0:
        return string + string[::-1]
    return string[:left] + string[:left:-1] + string[left:]

