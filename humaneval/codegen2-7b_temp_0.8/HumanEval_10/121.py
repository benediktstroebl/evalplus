

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
    if string is None or len(string) <= 0:
        return string

    string = string.lower()

    while True:
        start = 0
        end = len(string) - 1

        while start < end and string[start] == string[end]:
            start += 1
            end -= 1

        if start == end and string[start] == string[start + 1]:
            string = string[:start] + string[:start + 1]
        else:
            string += string[:start] + string[end + 1:][::-1]
            break

    return
