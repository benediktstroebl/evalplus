

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
    def find_palindrome_suffix(string: str) -> str:
        """ Find the longest palindromic suffix of a given string. """
        def find_palindrome_prefix(string: str) -> str:
            """ Find the longest palindromic prefix of a given string. """
            if len(string) < 2:
                return string

            first, middle, last = string[0], string[1:-1], string[-1]

            if first == last and is_palindrome(middle):
                return first + find_palindrome_prefix(middle) + last
            else:
                return find_palindrome_prefix(middle) + last

        return find_palindrome_prefix(string)[::-1]

    palindrome = find_palindrome_suffix(string)
    return string + palindrome[len(palindrome) // 2 + len(string) % 2:]

