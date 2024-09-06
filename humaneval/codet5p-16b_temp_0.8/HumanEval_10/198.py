

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

    if is_palindrome(string):
        return string
    else:
        prefix = ''
        palindromic_suffix = ''
        prefix_list = []
        for i, char in enumerate(string):
            if is_palindrome(string[i:]):
                palindromic_suffix = string[i:]
                prefix_list.append(palindromic_suffix)
            else:
                prefix_list.append(palindromic_suffix)
        if not prefix_list:
            return string
        if len(prefix_list) == 1:
            return prefix + prefix_list[0]
        max_len = max([len(prefix) for prefix in prefix_list])
        for prefix in prefix_list:
            if len(prefix) == max_len:
                return prefix + string[:-len(prefix)]
        return ''.join(prefix_list)

