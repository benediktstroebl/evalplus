

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

    def get_longest_palindromic_postfix(string):
        for i in range(len(string) // 2, 0, -1):
            if is_palindrome(string[len(string) - i:]):
                return string[len(string) - i:]
        return ""

    def get_shortest_palindromic_prefix(string):
        i = 0
        while i < len(string):
            if not is_palindrome(string[:i]):
                i += 1
            else:
                break
        return string[:i]

    longest_palindromic_postfix = get_longest_palindromic_postfix(string)
    shortest_palindromic_prefix = get_shortest_palindromic_prefix(string)
    return shortest_palindromic_prefix + longest_palindromic_postfix[::-1]

