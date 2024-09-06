

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
    # Step 1: find longest postfix of the string that is a palindrome
    palindrome_length = max([len(s) for s in re.findall(r'[^\W\d_]+', string) if is_palindrome(s)])
    
    # Step 2: append reverse of the prefix that comes before the palindromic suffix
    prefix = string[:palindrome_length]
    suffix = string[palindrome_length:]
    return prefix + string[::-1][::-1] + suffix

