

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
    string = string.strip()
    if not string:
        return ''

    is_palindrome_func = lambda string: is_palindrome(string)

    def search_palindrome(string, is_palindrome_func=is_palindrome_func):
        """ Find the longest palindromic substring """
        if string:
            mid = len(string) // 2
            if is_palindrome_func(string[:mid]):
                result = search_palindrome(string[mid:])
            else:
                result = search_palindrome(string[:mid]) + string[mid:]
            return result
        return ''

    return search_palindrome(string) + search_palindrome(string[:-1][::-1])

