

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

    palindromes = ['']  # the output array
    for i, letter in enumerate(string):
        for palindrome in palindromes[:]:
            if is_palindrome(palindrome + letter):
                palindromes.append(palindrome + letter)
    if is_palindrome(palindromes[-1]):
        return palindromes[-1]
    return ""  # empty string is a palindrome

