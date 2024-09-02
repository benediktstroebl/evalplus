

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
    suffix = string[::-1]
    longest_palindrome = ''
    for i in range(len(string)):
        for j in range(i, len(string)):
            test_string = string[i:j+1]
            if is_palindrome(test_string):
                if len(test_string) > len(longest_palindrome):
                    longest_palindrome = test_string
    return string + longest_palindrome[::-1]

