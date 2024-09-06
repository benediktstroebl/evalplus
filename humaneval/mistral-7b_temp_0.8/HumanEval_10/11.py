

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
    if string == '':
        return ''
    palindrome_string = string[::-1]
    if is_palindrome(string):
        return string
    index = 0
    while index < len(palindrome_string):
        if is_palindrome(palindrome_string[index:]):
            prefix = string[0: index]
            suffix = string[index:]
            return prefix + suffix[::-1]
        index += 1
    raise ValueError("No palindromes found for string")

