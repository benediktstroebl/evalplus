

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

    # reverse supplied string and add to the end
    reverse_string = string[::-1]
    string_with_reverse = string + reverse_string

    # iterate over the string and check if the prefix is palindrome.
    # if it is - we found our palindromic suffix.
    palindrom_suffix_length = 0
    for i in range(len(string_with_reverse)):
        if is_palindrome(string_with_reverse[i:]):
            palindrom_suffix_length = i

    # make a slice of the string that goes from beginning to palindromic suffix and reverse it
    return reverse_string[palindrom_suffix_length:] + string

