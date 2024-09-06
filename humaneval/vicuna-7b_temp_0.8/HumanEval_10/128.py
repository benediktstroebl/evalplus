

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
    string = string + 'c'  # Make the longest prefix of the string a palindrome
    prefix_len = len(string) // 2
    suffix_len = len(string) - prefix_len
    suffix = string[-suffix_len:]
    prefix = string[:prefix_len]
    if is_palindrome(prefix) and is_palindrome(suffix):
        return string
    else:
        for char in suffix:
            string = string[:-1]  # remove suffix
            if is_palindrome(string):
                if char not in string:
                    return string + char
                else:
                    return string
        return ''

