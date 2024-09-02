

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
    prefix = 'a'
    suffix = 'z'
    suffix_len = 26
    reverse_suffix = ''
    for char in string:
        if is_palindrome(char):
            # if char is a palindrome, we can just return it
            return string
        if char in prefix + suffix:
            # if char is in the prefix and suffix, we can append a reverse char
            reverse_suffix += string[::-1][::-1]
            suffix_len -= 1
            suffix = suffix[:-1]
            prefix = prefix[::-1]
            if suffix_len == 0:
                return string + reverse_suffix
            # if we've found a palindrome suffix, append it to the end of the string
            prefix = prefix[::-1]
            suffix = suffix[::-1]
            suffix_len = 0
    return string

