

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
    string = string + '
'  # Add space to the end of the string to get the longest palindrome
    max_len = 0
    for i in range(len(string) + 1):
        suffix = string[-i:].split('')
        prefix = string[:-i].split('')
        if len(suffix) > len(prefix):
            # This suffix is a palindrome
            suffix_reversed = ''.join(suffix[::-1])
            prefix_reversed = ''.join(prefix[::-1])
            # If suffix and prefix are not same, then we append them to get the final string
            if suffix_reversed != prefix_reversed:
                suffix = suffix[::-1] + suffix_reversed
                prefix = prefix_reversed + prefix[:-1]
            # Update the maximum length of palindrome
            max_len = max(max_len, len(suffix) + len(prefix_reversed))
    return ''.join(prefix) + suffix + ' '  # Create the final string

