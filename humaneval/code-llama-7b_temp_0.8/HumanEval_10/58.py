

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
    if not is_palindrome(string):
        # find the longest palindromic suffix of the supplied string
        suffix = string[::-1]
        longest_palindrome = ''
        for index in range(len(string)):
            if is_palindrome(string[index:]):
                if len(string[index:]) > len(longest_palindrome):
                    longest_palindrome = string[index:]

        prefix = string[:len(string) - len(longest_palindrome)]
        return prefix + longest_palindrome[::-1]
    return string

