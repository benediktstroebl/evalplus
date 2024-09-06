

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
    postfix = ''
    for char in string:
        postfix += char

    palindrome = ''
    while len(postfix) > 0:
        for index, char in enumerate(postfix):
            if is_palindrome(postfix[:index + 1]):
                palindrome += char
                postfix = postfix[index + 1:]
                break
        else:
            break

    palindrome += postfix[::-1]
    return palind
