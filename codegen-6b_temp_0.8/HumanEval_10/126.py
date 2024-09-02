

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
    longest = len(string)
    for i in range(len(string)):
        for j in range(len(string) - i, len(string)):
            postfix = string[i:j + 1]
            if is_palindrome(postfix):
                if j + 1 - i < longest:
                    longest = j - i + 1
                    res = postfix + string[:i:-1]
    return res

