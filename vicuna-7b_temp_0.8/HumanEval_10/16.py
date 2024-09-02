

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
    if string:
        # Find the longest postfix of supplied string that is a palindrome
        max_len = 0
        max_palindrome = ''
        for i in range(len(string)):
            if is_palindrome(string[i:]) and string[i:].upper() != string[i:].lower():
                max_len = i
                max_palindrome = string[i:].upper() + max_palindrome
        max_len_i = len(max_palindrome) - max_len
        max_palindrome_reversed = max_palindrome[::-1]
        new_string = string[:max_len_i] + max_palindrome_reversed + string[max_len_i:]
        
        # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
        prefix = string[:new_string.find(max_palindrome)]
        return prefix + new_string[new_string.find(max_palindrome) + len(max_palindrome):]
    return string

