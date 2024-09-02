

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

    try:
        if not is_palindrome(string):
            palindrome = ''
            max_palindrome = find_longest_palindrome(string)
            max_palindrome_start = string.index(max_palindrome)
            palindrome = string[max_palindrome_start::-1] + string
            return palindrome
    except TypeError:
        print("No palindrome found.")
        return None

