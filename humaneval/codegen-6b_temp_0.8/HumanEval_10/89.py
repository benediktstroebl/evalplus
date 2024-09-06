

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
    if not is_palindrome(string):
        return string + string[::-1]

    # better to not work this way, but whatever...
    # for i in range(len(string), 1, -1):
        # if is_palindrome(string[0:i]):
            # return string[0:i] + string[0:i][::-1]

    # better to not work this way, but whatever...
    # for i in range(len(string), 1, -1):
        # for j in range(len(string) - 1, i - 1, -1):
            # if is_palindrome(string[j:i]):
                # return string[j:i] + string[0:j][::-1]

    # better to not work this way, but whatever...
    # for i in range(len(string), 1, -1):
        # for j in range(len(string) - 1, i - 1, -1):
            # if is_palindrome(string[j:i]):
                # return string[j:i] + string[0:j - 1][::-1] + string[j - 1]

    # better to not work this way, but whatever...
    # for i in range(len(string), 1, -1):
        # for j in range(len(string) - 1, i - 1, -1):
            # if is_palindrome(string[j:i]):
                # return string[j:i] + string[0:j - 1][::-1] + string[j - 1] + string[0:j - 1][::-1]

    # better to not work this way, but whatever...
    # for i in range(len(string), 1, -1):
        # for j in range(len(string) - 1, i - 1, -1):
            # if is_palindrome(string[j:i] + string[0:j - 1][::-1] + string[j - 1]):
                # return string[j:i] + string[0:j - 1][::-1] + string[j - 1]

    