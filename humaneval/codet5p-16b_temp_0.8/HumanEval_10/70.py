

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

    if string == '':
        return ''

    palindromes_in_string = {}
    for i in range(1, len(string)+1):
        postfix = string[-i:]
        if is_palindrome(postfix):
            palindromes_in_string[i] = postfix

    length_of_longest_palindrome = max(palindromes_in_string.keys())
    longest_palindrome = palindromes_in_string[length_of_longest_palindrome]
    return string + longest_palindrome[::-1][:-1]

