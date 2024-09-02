

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
    longest_prefix = ''
    for char in string:
        longest_prefix += char
    palindromes = []
    for i in range(len(longest_prefix)):
        suffix = longest_prefix[i:]
        if is_palindrome(suffix):
            palindromes.append(suffix)
        else:
            break
    for j in range(len(palindromes)):
        string += palindromes[j]
    return string
