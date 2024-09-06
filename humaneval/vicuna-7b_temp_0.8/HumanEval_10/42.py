

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
    length = len(string)
    palindrome = ''
    for i in range(length // 2):
        if is_palindrome(string[i:(i + 1)]) and string[i:(i + 1)] != string[0:i]:
            palindrome += string[i:(i + 1)]
            break
    if length % 2 == 0:
        palindrome += string[0:length // 2]
    return palindrome

