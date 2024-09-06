

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

    from re import finditer

    if not is_palindrome(string):
        print('Input string is not a palindrome!')
        return string

    if len(string) < 2:
        print('Input string is too short!')
        return string

    palindrome = string[0]
    longest_palindrome = string[0]
    longest_palindrome_length = len(longest_palindrome)

    for match in finditer(r'(?=.*[a-z])(?=[A-Z][A-Z]|$)(?!^[a-z])([a-z0-9]+)', string):
        postfix_length = len(match.group())
        if postfix_length > longest_palindrome_length:
            longest_palindrome_length = postfix_length
            longest_palindrome = match.group()
        if postfix_length % 2 == 0:
            palindrome += match.group()[::-1]
        else:
            palindrome += match.group()[
