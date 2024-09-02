

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
    string += '$'
    palin = '$'
    for i in range(1, len(string)):
        min_palin = ''
        for j in range(1, i+1):
            palin_substr = string[-j : -j+i]
            if is_palindrome(palin_substr):
                if len(palin_substr) < len(min_palin):
                    min_palin = palin_substr
        if min_palin:
            palin = string[-len(min_palin)+1 : -len(min_palin)+1+i] + palin
    return palin

