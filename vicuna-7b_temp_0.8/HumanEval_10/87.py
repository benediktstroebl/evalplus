

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
    max_len = len(string)
    prefix = string[:max_len]
    suffix = string[max_len-1:]
    suffix_len = len(suffix)
    for suffix in [suffix[::-1] for suffix in suffix]:
        postfix = string + suffix
        if postfix == suffix[::-1]:
            postfix_len = len(postfix)
            if postfix_len > max_len - suffix_len:
                max_len = max_len - suffix_len
                prefix = string[:max_len]
                suffix = postfix[:max_len]
                return prefix + postfix[max_len-1:]
    return prefix + suffix[1:]
