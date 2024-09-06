

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
    if len(string) == 0:
        return ''
    else:
        # Find the longest postfix of the input string that is a palindrome
        palindrome_len = max(len(s) for s in find_palindromes(string))

        # Repeat the prefix backwards until it matches the postfix
        prefix = string[:palindrome_len]
        suffix = string[-palindrome_len:]
        while not prefix == suffix[::-1]:
            prefix = prefix[1:]
            suffix = suffix[:-1]
        return prefix + suffix[::-1]
