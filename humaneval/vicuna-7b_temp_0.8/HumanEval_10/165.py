

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
    result = ""
    string_len = len(string)
    palindromic_suffix = string[-(string_len - 1):]
    longest_postfix = "".join(string[0:-1])
    if len(longest_postfix) > len(palindromic_suffix):
        longest_postfix += palindromic_suffix[::-1]
    else:
        longest_postfix = palindromic_suffix
    result = longest_postfix + string[0]
    return result

