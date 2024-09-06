

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
    # initialize empty string
    palindrome = ""
    # create list of characters from the given string
    chars = list(string)
    # walk backwards through the string
    for i in range(len(chars) - 1, -1, -1):
        # walk forward to the next palindrome
        for j in range(i + 1, len(chars)):
            # if string after j is a palindrome
            if is_palindrome(chars[j:]):
                # reverse string before j and append it to the palindrome
                palindrome = chars[:j][::-1] + palindrome + chars[j:]
                break
    return palindrome

