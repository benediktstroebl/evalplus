

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
    longest_palindrom = string
    for i in range(len(string)):
        while string[i]!= string[i+1] and string[i]!= '':
            i += 1
        if string[i]!= string[i+1]:
            continue
        else:
            longest_palindrom = string[:i+1] + string[i+1:i]
    return longest_palindrom + string + string[::-1]

