

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
    longest_palindrome = None
    for i in range(len(string)):
        postfix_of_palindrome = string[i:] + string[:i][::-1]
        if is_palindrome(postfix_of_palindrome):
            if longest_palindrome is None or len(postfix_of_palindrome) > len(longest_palindrome):
                longest_palindrome = postfix_of_palindrome
    return string + longest_palindrome[::-1
