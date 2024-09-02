

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
    # We want to find the shortest string prefix that is a palindrome
    # If the length of the string is zero, we have a zero-length palindrome
    if len(string) == 0:
        return string
    # Find the longest suffix that is a palindrome
    # We find this by checking if the string suffix is a palindrome
    while not is_palindrome(string):
        suffix_len = len(string)
        # We traverse backwards through the string
        for i in range(len(string)-1, -1, -1):
            if is_palindrome(string[i:]):
                # If the suffix is a palindrome, we break out of the loop
                # and we add the prefix of the suffix to the end of the string
                suffix_len = i + 1
                break
        # Append the suffix to the start of the string
        string = string[:suffix_len] + string[suffix_len:]
    return string

