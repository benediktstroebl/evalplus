

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
    if not string:
        return string

    prefix = RE_PALINDROME_PREFIX.findall(string)
    if prefix:
        # Find the length of the longest palindromic substring, then use the length of the substring
        # and the string's length to calculate the start index
        substring_start = len(prefix[0]) + len(prefix[-1]) + 2
        palindrome_start = len(string) - len(prefix[-1]) - 1
        palindrome_end = len(string) - len(prefix[0]) - 1
        while palindrome_start > substring_start:
            substring = string[substring_start:palindrome_end + 1]
            if is_palindrome(substring):
                return string[:substring_start] + substring + string[palindrome_end + 1:]
            palindrome_start -= 1
            palindrome_end += 1
        return string
    return string

