

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
        return ''
    # Reverse given string
    rev_string = string[::-1]

    # Find the longest palindrome suffix
    i = 1
    while (i <= len(string)):
        if is_palindrome(string[0:i]):
            break
        i += 1
    # Check if a palindrome suffix was found
    if i > len(string):
        return string + rev_string

    # Reverse of prefix string that comes before the palindromic suffix
    pref = rev_string[0:len(string)-i+1][::-1]

    # Concatenate prefix to supplied string
    return pref + string

