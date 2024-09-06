

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
    # finding the longest palindrome prefix
    prefix = ''.join(sorted(string))
    if len(prefix) >= len(string):
        # the prefix is a palindrome
        return prefix
    else:
        # try to reverse the prefix to make a palindrome
        rev_prefix = ''.join(sorted(string[1:]))
        if is_palindrome(rev_prefix):
            # add the prefix to the end of the reverse of the prefix
            return string[:-len(rev_prefix)] + rev_prefix
        else:
            # try to reverse the prefix again to make a palindrome
            rev_prefix = ''.join(sorted(string[::-1]))
            if is_palindrome(rev_prefix):
                # add the prefix to the end of the reverse of the prefix
                return string[:-len(rev_prefix)] + rev_prefix
            else:
                # try to concatenate the prefix with another palindrome
                palindromes = get_palindromes(string)
                if len(palindromes) > 0:
                    palindrome = min(palindromes, key=len)
                    return string[:-len(palindrome)] + palindrome
                else:
                    return string

