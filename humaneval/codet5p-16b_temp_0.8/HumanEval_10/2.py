

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

    max_palindrome_len = 0
    palindrome_prefix = ''
    for substring in range(len(string)):
        substring_len = len(string[substring::])
        palindrome_prefix = string[:substring]
        substring_palindrome = palindrome_prefix + string[::-1][:substring_len][::-1]
        if is_palindrome(substring_palindrome):
            max_palindrome_len = substring_len
            break
    return string + palindrome_prefix[::-1][:max_palindrome_len]

