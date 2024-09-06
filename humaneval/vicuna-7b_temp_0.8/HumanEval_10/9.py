

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
    # Find the longest postfix that is a palindrome
    palindrome = re.findall(r'(.{1,})(?=.)', string)[0]
    string_prefix = string[:len(palindrome)].rjust(len(palindrome), '0')
    string_suffix = re.findall(r'(.{1,})(?=.)', palindrome)[0]
    # Append the reverse of the prefix that comes before the suffix
    string_new = string_prefix[:-len(palindrome)] + string_suffix[::-1] + string_prefix[-len(palindrome):]
    return string_new