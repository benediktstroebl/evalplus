

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
    # We need to find the longest suffix that is a palindrome
    # We can use Rabin-Karp for that

    # Find the longest suffix that is a palindrome
    len_str = len(string)
    if len_str <= 1:
        return string

    # Check if it is already a palindrome
    if is_palindrome(string):
        return string
    elif len_str == 2:
        return string[:1] + string[1:][::-1]

    candidate = ''
    for i in range(len_str - 1, 0, -1):
        # NOTE: Since the suffix is already a palindrome, we'll only check the prefix
        #       This will result in more accurate results
        if is_palindrome(string[len_str-i:]):
            if len(candidate) < len(string) - i + 1:
                candidate = string[len_str - i + 1:]
            break

    # We know that all characters before the suffix are also palindrome
    return candidate + string[:len_str - len(candidate)][::-1]
