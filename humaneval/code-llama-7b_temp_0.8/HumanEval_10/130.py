

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
    # compute the length of the given string
    length = len(string)

    # loop from the beginning of the given string to its end
    for i in range(length):
        # compute the length of the suffix
        suffix_length = length - i

        # if the given string is already a palindrome, we are done
        if is_palindrome(string[:suffix_length]):
            return string + string[:(length - i)]

    # if the loop completes, there is no palindrome and an exception is raised
    raise ValueError(f"The string {string} cannot be turned into a palindrome")
