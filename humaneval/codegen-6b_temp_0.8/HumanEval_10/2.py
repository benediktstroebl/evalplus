

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
    if string[0] == 'a' and string[-1] == 'a':
        return string
    elif string[0] == 'b' and string[-1] == 'b':
        return string
    elif string[0] == 'c' and string[-1] == 'c':
        return string
    elif string[0] == 'd' and string[-1] == 'd':
        return string
    elif string[0] == 'e' and string[-1] == 'e':
        return string
    elif string[0] == 'f' and string[-1] == 'f':
        return string
    elif string[0] == 'g' and string[-1] == 'g':
        return string
    elif string[0] == 'h' and string[-1] == 'h':
        return string
    elif string[0] == 'i' and string[-1] == 'i':
        return string
    elif string[0] == 'j' and string[-1] == 'j':
        return string
    elif string[0] == 'k' and string[-1] == 'k':
        return string
    elif string[0] == 'l' and string[-1] == 'l':
        return string
    elif string[0] == 'm' and string[-1] == 'm':
        return string
    elif string[0] == 'n' and string[-1] == 'n':
        return string
    elif string[0] == 'o' and string[-1] == 'o':
        return string
    elif string[0] == 'p' and string[-1] == 'p':
        return string
    elif string[0] == 'q' and string[-1] == 'q':
        return string
    elif string[0] == 'r' and string[-1] == 'r':
        return string
    elif string[0] == 's' and string[-1] == 's':
        return string
    elif string[0] == 't' and string[-1] == '