

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
    string = string.lower()
    longest_postfix = ""
    for i in range(len(string)):
        for j in range(len(string)):
            if (i == j) and is_palindrome(string[i:] + string[:i]):
                longest_postfix = string[i:] + string[:i]
                break
            else:
                longest_postfix = string[i]
    return longest_postfix + string[::-1]

