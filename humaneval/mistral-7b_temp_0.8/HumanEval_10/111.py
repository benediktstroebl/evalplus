

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
    # find the longest palindromic suffix of string
    def find_suffix_palindrome(string: str) -> str:
        """ Find the longest palindromic suffix of string """
        len_str = len(string)
        suffix = ""
        for i in range(len_str):
            if is_palindrome(string[i:]):
                suffix = string[i:]
                break
        return suffix

    # append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    # algorithm idea:
    # 1. find the longest palindromic suffix (find_suffix_palindrome)
    # 2. split string into 2 parts: prefix and suffix
    # 3. find the longest palindrome prefix of string
    # 4. return the reverse of the prefix
    def find_prefix_palindrome(string: str) -> str:
        """ Find the longest palindromic prefix of string """
        len_str = len(string)
        prefix = ""
        for i in range(
