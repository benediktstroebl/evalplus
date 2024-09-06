

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
    def make_subpalindrome(start: int, end: int) -> str:
        return string[start:end][::-1] + string

    def find_palindromic_substring_postfix(start: int) -> Tuple[int, int]:
        for end in range(start, len(string)):
            if is_palindrome(make_subpalindrome(start, end + 1)):
                return (start, end + 1)
        return (start, len(string))

    def find_palindromic_substring_prefix(end: int) -> Tuple[int, int]:
        for start in range(end - 1, -1, -1):
            if is_palindrome(make_subpalindrome(start, end)):
                return (start, end)
        return (-1, end)

    if not string:
        return string
    (start, end) = find_palindromic_substring_postfix(0)
    (start2, end2) = find_palindromic_substring_prefix(end)
    return string if start2 < 0 else string[:start2 + end2] + string[start:end]

