

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
    # base case, if string is empty or already a palindrome
    if string == '' or is_palindrome(string):
        return string
    else:
        # find the longest prefix that is a palindrome
        for i in range(len(string)):
            palindromic_suffix = string[i:][::-1]
            if is_palindrome(palindromic_suffix):
                return string[:i] + palindromic_suffix
        # no prefix found that is a palindrome
        return string + string[:0][::-1]


assert make_palindrome('cat') == 'catac'
assert make_palindrome('cata') == 'catac'
assert make_palindrome('') == ''
assert make_palindrome('aiou') == 'aiou'
assert make_palindrome('  t                      ') == '  t                      '
assert make_palindrome('abcdcba') == 'abcdcba'
assert make_palindrome('aaaa') == 'aaaa'
assert make_palindrome('aaaaa') == 'aaaaa'
assert make_palindrome('aaaaaa') == 'aaaaaa'
assert make_palindrome('aaaaaab') == 'aaaaaa'
assert make_palindrome('aaaaaaba') == 'aaaaaaaba'
assert make_palindrome('aaaaaabb') == 'aaaaaaabb'
assert make_palindrome('aaaaaabbb') == 'aaaaaaabbb'
assert make_palindrome('aaaaaabbba') == 'aaaaaaabbba'

assert is_palindrome('abcdecba') == True
assert is_palindrome('abba') == True
assert is_palindrome('abcd') == False
assert is_palindrome('cba') == True
assert is_palindrome('abba') == False

assert make_palindrome('abcda') == 'bdca'
