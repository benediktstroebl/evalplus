

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

    palindrome = ''
    palindromic_suffix = ''
    length = len(string)
    palindrome_candidates = []
    for i in range(length):
        for j in range(i+1, length+1):
            if is_palindrome(string[i:j]):
                palindromic_suffix = string[i:j]
                palindrome_candidates.append(palindromic_suffix)
    longest_palindromic_suffix = sorted(palindrome_candidates, key=len, reverse=True)[0]
    longest_palindromic_prefix = string[:-(len(longest_palindromic_suffix))]
    return longest_palindromic_prefix + longest_palindromic_suffix

