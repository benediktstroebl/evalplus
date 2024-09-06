

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
    s_len = len(string)
    if s_len == 1:
        return string

    postfix_len = 0
    for i in range(s_len // 2):
        if string[i] == string[s_len - i - 1]:
            postfix_len += 1
        else:
            break
    if postfix_len == s_len:
        return string

    prefix_len = s_len - 1 - postfix_len
    return string[:prefix_len] + string[s_len - postfix_len:][::-1]

