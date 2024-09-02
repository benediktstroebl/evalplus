

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
    # Find the longest postfix of supplied string that is a palindrome
    # string[j:i] is the longest suffix of supplied string that is also a palindrome
    j = len(string)

    while j :
        s1 = string[:j]
        if is_palindrome(s1):
            break
        else:
            j -= 1

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    s = s1[::-1] + string[j:]

    # Capitalize the first letter of each word in the string
    s = ''.join(word.capitalize() for word in s.split())

    return s

