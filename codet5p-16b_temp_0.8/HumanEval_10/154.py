

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

    longest_palindrome = is_palindrome(string)
    length_of_longest_postfix = 0
    index_of_longest_postfix = 0
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            length_of_longest_postfix = len(string[i:])
            index_of_longest_postfix = i
    if longest_palindrome:
        return string
    else:
        return string[:index_of_longest_postfix] + string[index_of_longest_postfix:index_of_longest_postfix-length_of_longest_postfix:-1]

