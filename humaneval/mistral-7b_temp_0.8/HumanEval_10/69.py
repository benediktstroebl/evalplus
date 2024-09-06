

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
    string = string.lower()

    def is_palindrome_substring(suffix: str) -> bool:
        return s.lower() == s[::-1]

    def find_longest_palindrome_substring(start: int) -> int:
        max_len = 0
        for i in range(start, len(s)):
            if is_palindrome_substring(s[start: i + 1]):
                max_len = i - start + 1
        return max_len

    s = string

    while not is_palindrome(s):
        if len(s) < 2:
            return s

        prefix = s[:find_longest_palindrome_substring(0)]
        suffix = s[find_longest_palindrome_substring(0) : ]

        s = (prefix[::-1] + suffix).lower()

    return s
