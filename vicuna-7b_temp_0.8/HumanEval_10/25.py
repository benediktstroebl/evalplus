

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
    if not string:
        return string
    elif string[0] == string[-1]:
        return string[::-1]
    else:
        prefix = []
        for char in string:
            if char == char[::-1]:
                prefix.append(char)
        suffix = string[1:]
        suffix_len = len(suffix)
        while suffix_len > 0:
            prefix_len = len(prefix)
            if suffix_len <= prefix_len:
                prefix.append(suffix[-1])
                suffix.pop()
                suffix_len -= 1
            elif suffix_len == prefix_len + 1:
                suffix.pop()
                suffix_len -= 1
            else:
                suffix.pop(0)
                suffix_len -= 1
        return ''.join(prefix) + string[::-1] + ''.join(suffix)

