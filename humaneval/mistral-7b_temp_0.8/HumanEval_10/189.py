

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
    def reverse(s: str) -> str:
        """ Return a reverse of given string. """
        return s[::-1]

    def get_longest_palindrome_postfix(string: str) -> str:
        """ Find the longest palindromic postfix of a given string. """
        start_index = len(string) - 1
        length = 0
        while start_index >= 0:
            end_index = start_index - 1
            while end_index >= 0:
                if string[start_index] == string[end_index]:
                    length = end_index - start_index + 1
                    start_index -= 1
                else:
                    end_index -= 1
                if length > 0:
                    break
        return string[start_index + 1: start_index + 1 + length]

    def reverse_prefix(prefix: str) -> str:
        """ Return the reverse of given prefix string. """
        return reverse(prefix)

    def find_palindrome(
