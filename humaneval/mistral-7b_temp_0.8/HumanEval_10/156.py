

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
    def get_longest_palindrome(string: str) -> str:
        """ Returns the longest palindrome in given string """
        if not string:
            return ""
        max_palindrome_len = 1
        current_palindrome = ""
        for i in range(len(string)):
            for j in range(i, len(string)):
                if is_palindrome(string[i:j + 1]):
                    if len(string[i:j + 1]) > max_palindrome_len:
                        max_palindrome_len = len(string[i:j + 1])
                        current_palindrome = string[i:j + 1]
        return current_palindrome

    def get_shortest_palindrome(string: str) -> str:
        """ Returns shortest palindrome for given string """
        if not string:
            return ""
        longest_palindrome = get_longest_palindrome(string)
        if len(longest_palindrome) == len(string
