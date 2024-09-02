

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
    org_string = string
    length = len(string)

    while True:
        # Find the longest postfix of supplied string that is a palindrome
        for i in range(length, 0, -1):
            if is_palindrome(string[:i]):
                break
        i -= 1
        if i == length:
            return org_string
        else:
            # Append to the end of the string reverse of a string prefix
            # that comes before the palindromic suffix.
            #
            # TEMPORARY: use indexes instead of slicing.
            # This seems to be faster using index instead of __getitem__, but
            # it might not work on other versions of Python eg. 2.7.14.
            string = string[:i][::-1] + string
            length = i

