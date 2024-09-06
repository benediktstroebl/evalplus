

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
    # 1. We start from the beginning and the end of the string and compare
    # each character to make sure they are the same
    # 2. If they are the same, move both the begin and end pointers up one character
    # 3. Else, move the beginning pointer up one character and keep the end at the same position

    # if supplied string is a palindrome, just return it
    if is_palindrome(string):
        return string

    long_pfx = None
    long_sfx = None

    # go forward from both ends, and as long as two ends are the same, update
    # our longest prefix and suffix
    begin = 0
    end = len(string) - 1
    while begin <= end:
        if string[begin] == string[end]:
            if long_pfx is None:
                long_pfx = begin
            if long_sfx is None:
                long_sfx = end
            begin += 1
            end -= 1
        else:
            break

    # if we got to the middle, palindrome can't be formed, so return -1
    if long_pfx is None or long_sfx is None:
        return -1

    # form the palindrome by adding prefix to end of suffix
    # ex: 'cata' -> 'cata' + 'aca' -> 'catacaca'
    return string[long_pfx:] + string[long_pfx::-1]

