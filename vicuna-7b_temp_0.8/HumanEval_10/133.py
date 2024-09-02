

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
    palindromes = []
    for prefix in string:
        prefix_len = len(prefix)
        for suffix in string[prefix:]:
            suffix_len = len(suffix)
            palindrome_prefix = prefix[:-suffix_len]
            if is_palindrome(palindrome_prefix):
                suffix_reversed = string[::-1][:-suffix_len]
                if is_palindrome(suffix_reversed):
                    palindromes.append(prefix + suffix_reversed)
                    break
    return ''.join(palindromes)

