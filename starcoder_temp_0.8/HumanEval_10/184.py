

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

    def expand(string):
        left = 0
        right = len(string)
        while left < right:
            if is_palindrome(string[left:right]):
                yield (left, right)
                left += 1
            else:
                right -= 1

    for index, _ in expand(string):
        return string + string[index:][::-1]

    return string + string[::-1]

