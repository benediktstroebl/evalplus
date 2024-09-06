

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
    def is_palindrome_with_start(string: str, start: int) -> bool:
        """ Helper function to test if given string with start index is a palindrome """
        end = len(string) - 1 - start
        return string[start:end+1] == string[start:end+1][::-1]

    if is_palindrome(string):
        return string
    for i in range(1, len(string)):
        if is_palindrome_with_start(string, i):
            return string[:i] + string[i:][::-1] + string[:i]
    return string + string[::-1]

