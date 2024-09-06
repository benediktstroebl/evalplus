

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
    string_len = len(string)
    max_length = string_len
    palindromic_prefix = ''
    for i in range(1, string_len):
        if is_palindrome(string[i:]) and string[i:].find(string[0]) == 0:
            max_length = i
            palindromic_prefix = string[i:].rstrip()
            break
    if max_length > 0:
        result = string[:max_length] + string[max_length::-1]
    else:
        result = string[:1] + string[1::-1]
    return result

