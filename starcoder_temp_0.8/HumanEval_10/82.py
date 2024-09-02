

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
    def find_palindromic_postfix(string: str) -> Tuple[str, int]:
        """ Find longest palindromic postfix """
        for start_index, char in enumerate(string):
            end_index = start_index + 1
            while end_index <= len(string) and string[start_index] == string[-1 * end_index]:
                end_index += 1
            if end_index > start_index + 1:
                return string[start_index:], start_index
        return '', -1

    def find_longest_prefix(string: str) -> Tuple[str, int]:
        """ Find longest palindromic prefix """
        for start_index in reversed(range(len(string))):
            end_index = start_index + 1
            while end_index <= len(string) and string[start_index] == string[-1 * end_index]:
                end_index += 1
            if end_index > start_index + 1:
                return string[:end_index], end_index
        return '', -1

    postfix, postfix_start = find_palindromic_postfix(string)
    prefix, prefix_end = find_longest_prefix(string[:postfix_start])
    return prefix + string + prefix[::-1]
