

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
    if len(string) == 0:
        return ''

    # Find the longest postfix of supplied string that is a palindrome.
    # Algorithm idea is simple:
    # - Brute force to find all prefix of supplied string that is a palindrome.
    # - Find the shortest one taking into account only the characters prior to the
    #   first character that is not a palindrome.
    # - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    for i in range(0, len(string)):
        test_string = string[0:i]

        # test_string[::-1] counts the number of times to reverse the string
        if is_palindrome(test_string[::-1]) and len(test_string) > len(string):
            break

    # The reversed part of the string
    reversed_part = test_string[::-1]

    # Remove the chars from the beginning of the string until it is a palindrome
    # string[0:i] + reversed_part
    return string[0:i] + reversed_part
