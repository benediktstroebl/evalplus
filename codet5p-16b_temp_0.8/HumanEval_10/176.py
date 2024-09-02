

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

    postfix_index = 0
    postfix_palindrome = ''
    prefix_palindrome = ''
    for i in range(len(string)):
        if is_palindrome(string[postfix_index:]):
            postfix_palindrome = string[postfix_index:]
            postfix_index = i + 1
        else:
            prefix_palindrome += string[i]
    return prefix_palindrome + string[::-1]
