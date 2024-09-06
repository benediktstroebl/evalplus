

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

    # we will search for a palindrome in a string reversed character by character
    rev_string = string[::-1]

    # find the first index of string that differs in reversed string
    # Algorithm idea is that if we find that the first suffix of our string is not palindromic
    # no prefix before it can be palindromic, because palindromes are symmetric.
    for index, (letter, rev_letter) in enumerate(zip(string, rev_string)):
        if letter != rev_letter:
            break
    else:  # we didn't find any letters that differ
        index = len(string)

    # now we will look for the longest palindromic suffix of our reversed string
    # if the suffix is the same as prefix - we already have our palindrome
    for suffix_length in range(index, -1, -1):
        suffix = rev_string[:suffix_length]
        if suffix == suffix[::-1]:
            break

    # to get back our palindrome we need to reverse the suffix
    return string + suffix[::-1]

