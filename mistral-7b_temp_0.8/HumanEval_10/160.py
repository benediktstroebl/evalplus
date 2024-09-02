

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
    string = string.strip()
    if len(string) <= 1:
        return string

    def find_longest_palindrome_in_string(string: str) -> str:
        """ Find the longest palindrome in string """
        if len(string) <= 1:
            return ''
        # Palindrome can't start with odd number of chars
        if len(string) % 2 == 1:
            raise ValueError('String length is odd.')

        if is_palindrome(string):
            return string

        if not is_palindrome(string[:len(string) // 2]):
            return find_longest_palindrome_in_string(string[:len(string) // 2])
        elif not is_palindrome(string[1:len(string) // 2 + 1]):
            return find_longest_palindrome_in_string(string[1:len(string) // 2 + 1])
        else:
            return string[1:len(string) // 2 + 1
