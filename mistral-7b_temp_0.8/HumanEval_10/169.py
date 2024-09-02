

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
    def longest_palindromic_suffix(string: str) -> str:
        """ Find the longest palindromic suffix of a given string """
        if string == '':
            return ''
        if string[:2] == string[-2:][::-1]:
            return longest_palindromic_suffix(string[:-2])
        return string[len(string)-1] + longest_palindromic_suffix(string[:len(string)-1])

    def reverse_prefix(string: str) -> str:
        """ Reverse prefix of given string """
        if len(string) < 2:
            return string
        return reverse_prefix(string[1:]) + string[0]

    prefix = string
    palindromic_suffix = longest_palindromic_suffix(string)
    if is_palindrome(palindromic_suffix):
        return prefix + reverse_prefix(palindromic_suffix)
    else:
        return prefix + palindromic_suffix

