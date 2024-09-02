

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
    string = string.upper()
    if len(string) == 0:
        return 'a' * (2 if string.find('a') != -1 else 1)
    elif is_palindrome(string):
        return string
    else:
        max_len = 1
        for i in range(2, len(string)):
            if is_palindrome(string[i:]) and len(string[i:]) > max_len:
                max_len = len(string[i:])
        prefix = string[:max_len]
        suffix = string[max_len:]
        return prefix + 'b' + suffix[::-1].lower()

